These files are meant to be run as part of a pipeline using Lambda to grab tweets and store them in dynamodb
then the second is code used a jupiter notebook to analyze this data, pulling from the dynamodb table.

1. twitterCorpusBuilder.py is run 1/hour on Lambda and stores data in dynamodb
    note: we store twitter credentials in twitterConfig.py locally (note here for obvious reasons :))
2. jupiterNotebookSnippets.py is code snippets used on a sagemaker hosted jupiter notebook

