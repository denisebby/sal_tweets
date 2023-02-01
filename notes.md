video followed: https://www.youtube.com/watch?v=q8q3OFFfY6c

ssh -i "tweets_airflow_t3_med_key.pem" ubuntu@ec2-3-234-177-13.compute-1.amazonaws.com
airflow standalone
modify airflow.cfg accordingly

# additional steps I had to take
- I had to use t3 medium instance type for ec2 instance
- sudo chmod 600 tweets_airflow_t3_med_key.pem, this resolves permissions issues
- In order to connect to aws instance using public IPv4 DNS, I had to edit 
    security group and stop and restart instance

monitor ports:
- sudo lsof -i -P -n | grep LISTEN

kill all processes, clear ports:
- kill -15 -1