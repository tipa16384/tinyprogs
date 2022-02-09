(ns tinyprogs.clojure
  (:require [clojure.string :as string]))

(defn staircase2 [n]
  (doseq [i (range n)]
    (println (string/join
              (for [j (range n)] (if (< j (- n i 1)) " " "#"))))))

(defn staircase3 [n]
  (->> (for [i (range n)]
         (str (string/join (repeat (- n i 1) \space))
              (string/join (repeat (+ i 1) \#))))
       (run! println)))

(defn staircase [n]
  (->> (for [i (range n)]
         (str (string/join (repeat (dec (- n i)) \space))
              (string/join (repeat (inc i) \#))))
       (run! println)))

(staircase 6)
