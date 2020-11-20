;; Auto-generated. Do not edit!


(when (boundp 'chat_my2::test)
  (if (not (find-package "CHAT_MY2"))
    (make-package "CHAT_MY2"))
  (shadow 'test (find-package "CHAT_MY2")))
(unless (find-package "CHAT_MY2::TEST")
  (make-package "CHAT_MY2::TEST"))

(in-package "ROS")
;;//! \htmlinclude test.msg.html


(defclass chat_my2::test
  :super ros::object
  :slots (_s _x _y ))

(defmethod chat_my2::test
  (:init
   (&key
    ((:s __s) "")
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    )
   (send-super :init)
   (setq _s (string __s))
   (setq _x (float __x))
   (setq _y (float __y))
   self)
  (:s
   (&optional __s)
   (if __s (setq _s __s)) _s)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:serialization-length
   ()
   (+
    ;; string _s
    4 (length _s)
    ;; float32 _x
    4
    ;; float32 _y
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _s
       (write-long (length _s) s) (princ _s s)
     ;; float32 _x
       (sys::poke _x (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _y
       (sys::poke _y (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _s
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _s (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float32 _x
     (setq _x (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _y
     (setq _y (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get chat_my2::test :md5sum-) "773945f4ca27234189a5ae6671065ad3")
(setf (get chat_my2::test :datatype-) "chat_my2/test")
(setf (get chat_my2::test :definition-)
      "string s
float32 x
float32 y

")



(provide :chat_my2/test "773945f4ca27234189a5ae6671065ad3")


