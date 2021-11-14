<?php

/*
Plugin Name: Breadcrumb
Plugin URI: http://www.thedevproject.com/projects/wordpress-breadcrumb-plugin/
Description: Breadcrumb navigation for WordPress. Simply use &lt;?php breadcrumb(); ?&gt; within your template to display the breadcrumb anywhere on your site. If you need further help, visit the plugin web site.
Author: Dan Peverill
Version: 0.5.1
Author URI: http://www.thedevproject.com
*/

/*
    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program; if not, write to the Free Software
    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
*/

/**
* OPTIONS:
*
* breadcrumb() specific:
* sep, before, after, last, echo
*
* global:
* home_always, home_never, home_title
* link_all, link_none
*/

// Default breadcrumb filters.
add_filter("get_breadcrumb", "get_breadcrumb_home", 1, 2);
add_filter("get_breadcrumb", "get_breadcrumb_category", 5, 2);
add_filter("get_breadcrumb", "get_breadcrumb_page", 5, 2);
add_filter("get_breadcrumb", "get_breadcrumb_single", 5, 2);
add_filter("get_breadcrumb", "get_breadcrumb_date", 5, 2);
add_filter("get_breadcrumb", "get_breadcrumb_author", 5, 2);
add_filter("get_breadcrumb", "get_breadcrumb_search", 5, 2);
add_filter("get_breadcrumb", "get_breadcrumb_404", 5, 2);
add_filter("get_breadcrumb", "get_breadcrumb_paged", 5, 2);

/**
* @return bool
*/
function has_breadcrumb()
{
  global $wp_query;
  
  if (!$wp_query->is_home)
    return true;

  if (breadcrumb_is_paged())
    return true;
    
  return false;
}

/**
* @return bool
*/
function breadcrumb_is_paged()
{
  global $wp_query;

  return ((($page = $wp_query->get("paged")) || ($page = $wp_query->get("page"))) && $page > 1);
}

/**
* @param string Text to put inbetween crumbs. OR options in the format of key1=value1&key2=value2&key3=value3 and so on. If this is used, other params are ignored.
* @param string Text to put infront of a crumb.
* @param string Text to put behind a crumb.
* @param string Text to put infront of the current crumb (last crumb in the list, the users current location).
* @return string
*/
function breadcrumb($sep = "&raquo;", $before = "", $after = "", $last = "")
{
  global $wp_query;
  
  // Did the user use options?
  $options    = $sep;
  $echo       = false;
  $breadcrumb = array();
  
  parse_str($options, $params);
  if (count($params))
  {
    $sep    = isset($params["sep"]) ? $params["sep"] : "&raquo;";
    $before = isset($params["before"]) ? stripslashes($params["before"]) : "";
    $after  = isset($params["after"]) ? stripslashes($params["after"]) : "";
    $last   = isset($params["last"]) ? stripslashes($params["last"]) : "";
    $echo   = isset($params["echo"]) ? $params["echo"] : true;
  }
  else
  {
    $options = "";
  }

  $breadcrumb = get_breadcrumb($options);
  $count      = count($breadcrumb);

  for($i = 0; $i < $count; $i++)
  {
    if (!$last || ($i+1) < $count)
      $breadcrumb[$i] = $before . $breadcrumb[$i] . $after;
    else
      $breadcrumb[$i] = $last . $breadcrumb[$i] . $after;
  }
  
  $breadcrumb = implode(" ".$sep." ", $breadcrumb);
  
  if ($echo)
    print $breadcrumb;
  else
    return $breadcrumb;
}

/**
* Displays the breadcrumb for browser title use.
*/
function breadcrumb_title()
{
  breadcrumb("always_home=true&link_none=true&home_title=".bloginfo("name"));
}

/**
* @param string   Options in the format of key1=value1&key2=value2&key3=value3 and so on.
* @return array
*/
function get_breadcrumb($options = "")
{
  parse_str($options, $params);

  // Set defaults if no param specified.
  $params["link_all"]     = isset($params["link_all"]) ? $params["link_all"] : false;
  $params["link_none"]    = isset($params["link_none"]) ? $params["link_none"] : false;
  $params["home_always"]  = isset($params["home_always"]) ? $params["home_always"] : false;
  $params["home_never"]   = isset($params["home_never"]) ? $params["home_never"] : false;
  $params["home_title"]   = isset($params["home_title"]) ? $params["home_title"] : __("Home");
  
  $breadcrumb = array();
  $breadcrumb = apply_filters("get_breadcrumb", $breadcrumb, $params);

  return $breadcrumb;
}

/**
* @param array
* @param array
* @return array
*/
function get_breadcrumb_home($breadcrumb, $params)
{
  if ($params["home_never"])
    return $breadcrumb;
    
  global $wp_query;

  if (has_breadcrumb() || $params["home_always"])
  {
    if ((has_breadcrumb() || $params["link_all"]) && !$params["link_none"])
      $breadcrumb[] = '<a href="'.get_settings("home").'" title="'.get_settings("name").'">'.$params["home_title"].'</a>';
    else
      $breadcrumb[] = $params["home_title"];
  }
  
  return $breadcrumb;
}

/**
* @param array
* @param array
* @return array
*/
function get_breadcrumb_category($breadcrumb, $params)
{
  global $wp_query;

  if ($wp_query->is_category)
  {
    $object = $wp_query->get_queried_object();
  
    // Parents.
    $parent_id  = $object->category_parent;
    $parents    = array();
    while ($parent_id)
    {
      $category   = get_category($parent_id);
      
      if ($params["link_none"])
        $parents[]  = $category->cat_name;
      else
        $parents[]  = '<a href="'.get_category_link($category->cat_ID).'" title="'.$category->cat_name.'">'.$category->cat_name.'</a>';
      
      $parent_id  = $category->category_parent;
    }
    
    // Parents were retrieved in reverse order.
    $parents    = array_reverse($parents);
    $breadcrumb = array_merge($breadcrumb, $parents);
    
    // Current category.
    if ((breadcrumb_is_paged() || $params["link_all"]) && !$params["link_none"])
      $breadcrumb[] = '<a href="'.get_category_link($object->cat_ID).'" title="'.$object->cat_name.'">'.$object->cat_name.'</a>';
    else
      $breadcrumb[] = $object->cat_name;
  }
  
  return $breadcrumb;
}

/**
* @param array
* @param array
* @return array
*/
function get_breadcrumb_page($breadcrumb, $params)
{
  global $wp_query;

  if ($wp_query->is_page)
  {
    $object = $wp_query->get_queried_object();
  
    // Parents.
    $parent_id  = $object->post_parent;
    $parents    = array();
    while ($parent_id)
    {
      $page       = get_page($parent_id);
      
      if ($params["link_none"])
        $parents[]  = get_the_title($page->ID);
      else
        $parents[]  = '<a href="'.get_permalink($page->ID).'" title="'.get_the_title($page->ID).'">'.get_the_title($page->ID).'</a>';
      
      $parent_id  = $page->post_parent;
    }
    
    // Parents are in reverse order.
    $parents    = array_reverse($parents);
    $breadcrumb = array_merge($breadcrumb, $parents);
    
    // Current page.
    if ((breadcrumb_is_paged() || $params["link_all"]) && !$params["link_none"])
      $breadcrumb[] = '<a href="'.get_permalink($object->ID).'" title="'.get_the_title($object->ID).'">'.get_the_title($object->ID).'</a>';
    else
      $breadcrumb[] = get_the_title($object->ID);
  }
  
  return $breadcrumb;
}

/**
* @param array
* @param array
* @return array
*/
function get_breadcrumb_single($breadcrumb, $params)
{
  global $wp_query;

  if ($wp_query->is_single)
  {
    $object = $wp_query->get_queried_object();
  
    if ((breadcrumb_is_paged() || $params["link_all"]) && !$params["link_none"])
      $breadcrumb[] = '<a href="'.get_permalink($object->ID).'" title="'.get_the_title($object->ID).'">'.get_the_title($object->ID).'</a>';
    else
      $breadcrumb[] = get_the_title($object->ID);
  }
  
  return $breadcrumb;
}

/**
* @param array
* @param array
* @return array
*/
function get_breadcrumb_date($breadcrumb, $params)
{
  global $wp_query, $year, $monthnum, $month, $day;

  if ($wp_query->is_date)
  {
    // Year
    if ($wp_query->is_year || $wp_query->is_month || $wp_query->is_day)
    {
      if ($params["link_none"] || ($wp_query->is_year && !breadcrumb_is_paged() && !$params["link_all"]))
        $breadcrumb[] = $year;
      else
        $breadcrumb[] = '<a href="'.get_year_link($year).'" title="'.$year.'">'.$year.'</a>';
    }
  
    // Month.
    if ($wp_query->is_month || $wp_query->is_day)
    {
      $monthname = $month[zeroise($monthnum, 2)];
    
      if ($params["link_none"] || ($wp_query->is_month && !breadcrumb_is_paged() && !$params["link_all"]))
        $breadcrumb[] = $monthname;
      else
        $breadcrumb[] = '<a href="'.get_month_link($year, $monthnum).'" title="'.$monthname.'">'.$monthname.'</a>';
    }
  
    // Day.
    if ($wp_query->is_day)
    {
      if ($params["link_none"] || (!breadcrumb_is_paged() && !$params["link_all"]))
        $breadcrumb[] = $day;
      else
        $breadcrumb[] = '<a href="'.get_day_link($year, $monthnum, $day).'" title="'.$day.'">'.$day.'</a>';
    }
  }
  
  return $breadcrumb;
}

/**
* @param array
* @param array
* @return array
*/
function get_breadcrumb_author($breadcrumb, $params)
{
  global $wp_query;

  if (is_author())
  {
    $object = $wp_query->get_queried_object();
    
    if ($params["link_all"] || (breadcrumb_is_paged() && !$params["link_none"]))
      $breadcrumb[] = '<a href="'.$_SERVER["REQUEST_URI"].'" title="'.$object->display_name.'">'.$object->display_name.'</a>';
    else
      $breadcrumb[] = $object->display_name;
  }
  
  return $breadcrumb;
}

/**
* @param array
* @param array
* @return array
*/
function get_breadcrumb_search($breadcrumb, $params)
{
  global $wp_query;

  if (is_search())
  {
    if ((!breadcrumb_is_paged() && !$params["link_all"]) || $params["link_none"])
      $breadcrumb[] = get_breadcrumb_search_phrase();
    else
      $breadcrumb[] = '<a href="'.get_settings("home").'?s='.get_breadcrumb_search_uri().'" title="Search">'.get_breadcrumb_search_phrase().'</a>';
  }
  
  return $breadcrumb;
}

/**
* @param array
* @param array
* @return array
*/
function get_breadcrumb_404($breadcrumb, $params)
{
  global $wp_query;

  if ($wp_query->is_404)
  {
    if ($params["link_all"])
      $breadcrumb[] = '<a href="'.$_SERVER["REQUEST_URI"].'" title="404">404</a>';
    else
      $breadcrumb[] = "404";
  }
    
  return $breadcrumb;
}

/**
* @param array
* @param array
* @return array
*/
function get_breadcrumb_paged($breadcrumb, $params)
{
  global $wp_query;
  
  if ((($page = $wp_query->get("paged")) || ($page = $wp_query->get("page"))) && $page > 1)
  {
    if ($params["link_all"])
      $breadcrumb[] = '<a href="'.$_SERVER["REQUEST_URI"].'" title="Page "'.$page.'">Page '.$page.'</a>';
    else
      $breadcrumb[] = __("Page ").$page;
  }
    
  return $breadcrumb;
}

/**
* @return string
*/
function get_breadcrumb_search_phrase()
{
  return htmlentities(stripslashes($_GET["s"]), ENT_QUOTES);
}

/**
* @return string
*/
function get_breadcrumb_search_uri()
{
  return htmlentities(rawurlencode(stripslashes($_GET["s"])), ENT_QUOTES);
}

?>