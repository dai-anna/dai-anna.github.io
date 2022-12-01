---
type: pages
layout: single
title: Portfolio
permalink: /portfolio/
classes: wide
---
#  <img width=90 align="right" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Duke_University_logo.svg/1024px-Duke_University_logo.svg.png">

## Machine Learning and Deep Learning

**NLP Models Benchmarking**, Team Project ([GitHub](https://github.com/dai-anna/Duke-NLP-FinalProject) | [Research Report](https://github.com/dai-anna/Duke-NLP-FinalProject/blob/main/report/report_submission_flat.pdf))
- Collected data on seven different topics on twitter, leveraging Twint and Twitter API
- Built an LDA generative model as well as a discriminative Neural Network to benchmark their performance in topic classification

**Semi-supervised/Representation Learning Benchmarking**, WIP Team Project
- Implemented SimCLR and RotNet framework with ResNet20 to benchmark model performance on limited labeled CIFAR10 data
- Intend to also benchmark performance against adversarial attacks

**Deep Reinforcement Learning vs Deep Learning Recommendation Systems**, WIP Team Project
- Intend to benchmark performance of deep reinforcement learning recommender against deep learning recommender on two datasets

**Hybrid Recommendation System** ([GitHub](https://github.com/dai-anna/RenttheRunwayRecommendations) | [Research Report](https://github.com/dai-anna/RenttheRunwayRecommendations/blob/main/report/RTRRecommendationsFinalReport.pdf) | [Presentation](https://youtu.be/PzAVR38oM6Y))
- Developed hybrid recommendation system for fashion rental industry by first segmenting customers using unsupervised clustering methods then recommending items within each segment
- Benchmarked performance of hybrid system on the Rent the Runway dataset against making recommendations on the fullset and found improved performance in some segments

**Haiku Generator**, WIP ([GitHub](https://github.com/dai-anna/DeepLearning-HaikuGenerator))
- Intend to experiment with different deep learning models to tokenize corpus by syllables to generate Haikus using other deep learning NLP models


## Statistical Modeling 
**Compensation Analysis of the U.S. Technology Sector** ([GitHub](https://github.com/dai-anna/StackOverflow2021Survey-RegressionAnalysis) | [Research Report](https://github.com/dai-anna/StackOverflow2021Survey-RegressionAnalysis/blob/main/30_results/final_report.pdf))
- Used 2021 Stack Overflow Annual Survey data to regress total compensation of employed U.S. developers on experience and demographic variables to draw conclusions on if race or gender plays a significant role in receiving higher compensation
- Performed data cleansing using R scripts on self-reported survey data with multi-selection responses, significant missing data, and outliers to build a hierarchical linear regression model differing by US States

## Cloud Data Engineering
**AWS Cloud-Native Automatic Tweet Generator**, Team Project ([GitHub](https://github.com/dai-anna/AWSCloud-TweetGenerator))
- Built using Python an Amazon Web Service cloud-native end-to-end data-scraping and processing pipeline that automatically generates Tweets for currently trending hashtags with machine learning model (Hidden Markov and N-Gram model)
- Orchestrated pipeline to run daily, push to web application through Google Cloud Platform as well as post from Twitter bot through Twitter API
- Leveraged Python CDK (IaC), AWS Lambda, EventBridge, Batch, EC2 Spot Instance, ECR and S3 services as well as Docker containers
- Set up continuous integration and delivery pipeline through GitHub Actions and logging and monitoring pipeline in AWS

## Competition
**Duke Datathon**, Team Project - Winning Submission ([GitHub](https://github.com/unsupervisedlearner1123/Duke-Datathon-2021) | [Research Report](https://github.com/unsupervisedlearner1123/Duke-Datathon-2021/blob/main/40_docs/Report_final.pdf))
- Led team to augment and gain insight on Asian Barometer data by performing factor analysis to produce latent factors from survey questions, which we then predicted using demographic variables while keeping on track for the 24-hour turnaround
- Cleaned up and merged two large, messy datasets over two time periods using Python to get sense of progression over time

### Others
**Leaders in Fortune500**, WIP ([GitHub](https://github.com/dai-anna/Leadership-in-Fortune500))
- Web-scraped for data on leaders in Fortune500 companies (executive board members and c-suite)
- Constructed relational database with scraped data for further analysis
