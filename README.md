# sal_tweets
I wanted to build an ETL pipeline that ingests tweets of a specific person. I chose the comedian Sal Vulcano.

This uses Airflow to read in tweets into a csv file in an S3 bucket. I use EC2 to install and run Airflow. I use Tweepy to get tweets.