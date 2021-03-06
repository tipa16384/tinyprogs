var miniSprites;
var canvas;
var ctx;
var stage;
var carbm;
var fpsText;

var spriteSize = 128;
var fps = 50;
var cycle = 10000;
var carlen = 76;

var bPoint;

function getPoint(cx,cy,ang) {
  var p = new Object();
  p.cx = cx;
  p.cy = cy;
  p.ang = ang;
  return p;
}

// return a location in polar coordinates based on the current time
function getPos() {
  with (Math) {
    var td = Ticker.getTime(false);
    var theta = -((td % cycle)*2*PI)/cycle;
    var r = cos(2*theta);
    var x = 0.95 * r * cos(theta);
    var y = -0.95 * r * sin(theta);
    var t = theta + PI/2;
    return getPoint(x,y,t);
  }
}

// get the appropriate frame of the animation (from 0.0-1.0). chosen from the angle
// of the line connecting the center of the front axle (p1) to the center
// of the rear axle (p2). if the points are the same, return 0.

function getFrame(p1,p2) {
  var frame;
  
  if (p2.cx == p1.cx && p2.cy == p1.cy) {
    return 0;
  }
  
  if (p2.cx == p1.cx) {
    if (p2.cy < p1.cy) {
      frame = 0.75;
    } else {
      frame = 0.25;
    }
  } else if (p2.cy == p1.cy) {
    if (p2.cx > p1.cx) {
      frame = 0.0;
    } else {
      frame = 0.5;
    }
  } else {
    with(Math) {
      var dx = p2.cx - p1.cx;
      var dy = p2.cy - p1.cy;
      var dist = sqrt(dx*dx + dy*dy);
      var theta = acos(dx/dist);
      if (dy < 0) {
        theta = 2 * PI - theta;
      }
      frame = theta / (2*PI);
    }
  }
  return frame;
}

function translate(p) {
  var p2 = getPoint(0,0,0);
  var cw = canvas.getDimensions().width/2;
  var ch = canvas.getDimensions().height/2;
  var cx = cw + cw * p.cx;
  var cy = ch - ch * p.cy;
  p2.cx = cx;
  p2.cy = cy;
  return p2;
}

function turnCar() {
  drawCar();
}

function tick() {
    drawCar();        
    fpsText.text = "FPS: "+Math.round(Ticker.getMeasuredFPS());
    // update the stage:
    stage.update();
}

function drawCar() {
  var p;
  var d0;
  var dx, dy;
  var mult;
  
  p0 = bPoint;
  p = translate(getPos());
  
  dx = p.cx-p0.cx;
  dy = p.cy-p0.cy;
  
  d0 = Math.sqrt(dx*dx+dy*dy);
  p0.cy = p.cy - (carlen*dy)/d0;
  p0.cx = p.cx - (carlen*dx)/d0;
  
  var pframe = getFrame(p0,p);
  
  carbm.currentFrame = Math.round(144*pframe);
  carbm.x = (p.cx+p0.cx)/2-spriteSize/2;
  carbm.y = (p.cy+p0.cy)/2-spriteSize/2;
}

function loadSprites() {
  //get canvas element
  canvas = $('gameBoard');
  
  //get context
  ctx = canvas.getContext('2d');

  stage = new Stage(canvas);

  //create new image object
  miniSprites = new Image();

  //set callback for when the image actually loads
  //miniSprites.onload = startAnimation;
  
  //load the image
  miniSprites.src = "minisprites.png";
  
  var bg = new Image();
  bg.src = "bg.jpg";
  
  stage.addChild(new Bitmap(bg));
  
  var spriteSheet = new SpriteSheet(miniSprites,128,128);
  spriteSheet.loop = false;
  spriteSheet.totalFrames = 144;
  
  carbm = new BitmapSequence(spriteSheet);
  carbm.currentFrame = 0;
  carbm.paused = true;
  stage.addChild(carbm);
  
  fpsText = new Text("00","bold 36px Arial","#FF0");
  fpsText.x = 10; fpsText.y = 40;
  stage.addChild(fpsText);
  
  Ticker.addListener(window);
  Ticker.setFPS(fps);
  
  bPoint = getPoint(-1000,-1000,0);
}

Event.observe(window, "load", function() {
  loadSprites();
});
