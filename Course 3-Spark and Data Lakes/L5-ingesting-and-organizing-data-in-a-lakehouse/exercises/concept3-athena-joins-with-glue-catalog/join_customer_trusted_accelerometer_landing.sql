select * from "accelerometer_landing" 
join "customer_trusted"
on "accelerometer_landing"."user" = "customer_trusted"."email"