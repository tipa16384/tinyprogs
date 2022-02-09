(ns tinyprogs.clojure
  (:require [clojure.string :as string]))

(def n (Integer/parseInt (string/trim (read-line))))

(def arr (vec (map #(Integer/parseInt %) (string/split (clojure.string/trimr (read-line)) #" "))))

(comment (print (string/join \space (for [i (range n)] (nth arr (- n i 1))))))

(print (string/join \space (reverse arr)))
