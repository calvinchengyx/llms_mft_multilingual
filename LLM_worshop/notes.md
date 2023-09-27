# Oxford LLMs Workshop Notes
All notes are from the [Oxford LLMs workshop](https://www.llmsforsocialsciene.dev/) held on Sep 27-29, 2023. Thanks to [Maksim Zubok](https://www.llmsforsocialsciene.dev/posts/people/) for organizing. 

## Day -1. Preparation (Sep 25)
### Daily Tasks 
1. ~~Create a GitHub page to make notes of the workshop and store codes~~
2. ~~civic_j project summary~~
3. Clean-up civic_j codes, make it ready for open-repo
4. Get ready for your moral foundation paper, 
    1. ~~set the goal~~, `have a better understanding of LLMs and how to use it in works`
    2. make a to-do list this week 
5. Go through python tutorial in the workshop page 
6. 

### Civic_j project summary
#### Basic information
* __Task__: Classify the sentiment of tweets content (texts)
* __Language__: simplified Chinese
* __Domain/Context__: Protest (white paper movement in 2022)
* __Sentiment__: positive, negative and neutral
* __Classification__: the general sentiment + the entity sentiment 

#### Benchmarked Methods
* __Human Coders__: 3 expert native Chinese speakers with postgraduate degrees ($N=1,200$)
* __Dictionary__: [`ANTUSD`](https://aclanthology.org/L16-1428/), [`HowNet`](https://scholar.google.com/scholar_lookup?title=Sentiment%20analysis&publication_year=2010&author=Y.Y.%20Zhao&author=B.%20Qin&author=T.%20Liu), two most widly used Chinese sentiment dictionaries 
* __Machine/Deep Learning__: [erlangshen BERT](https://arxiv.org/abs/2209.02970), a fine-tuned Chinese BERT model for sentiment analysis
* __LLMs(OpenAI)__: GPT-3.5-turbo, curie, adas 

#### Key Takeaways
1. __Results__: `GPT-3.5-turbo` genearally outperformed dictionaries and BERT methods in terms of coverage, recall, precision, and accuracy, benchmarking with human coded golden standard. 
2. __Positive Implication__:
    1. LLMs need less annotated data than ML or DL methods to achieve acceptable results, e.g., I used 1k training records.
    2. LLMs is capable of dealing with multiple tasks at the same time, more efficient, e.g., I asked GPT to code 11 entities' sentiment in one request
    3. LLms can be trained with large datasets if needed, of course, with a bit expensive price.
3. __Other Implications and Questions__: 
    1. [Prompt enginnering](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/) is more effective in terms of increasing model performance than training with small amount of data (< 1k records). I spent much time trail the best-performance prompt, and followed the five-basic frameworks provided by OpenAI. `But not sure how the difference will be if we just train with large amount of data`
    2. `What does the training mean, for example in the GPT-3.5-turbo model`? I am not quite sure about the rationale and process of training a chat model. 
    3. Halluciation issue is quite prevalent. Very often the model will return a made-up result, in my case, it returns a sentiment towards an entity which is not mentioned at all in the given tweet. This is so common, almost 10% of result will have the issue, that i have to do another round of keyword matching to filer those `false results`. `how to deal with halluciation problem?` In other words, GPT-3.5-turbo acts really like a human and if you ask it to recode the task, the result might be different. It will depend on the temperature you set and how difficult the text is. 
    4. For general sentiment analysis methods, analyzing an overall sentiment of a piece does not make sense as it simplied the content in terms of meaning, but complicated the task in terms of coding. for example, if a tweet is positive in the first half, but negative in the second half, it is challenging to conclude an overal sentiment. So, we suggest using `entity-based sentiment analysis` only in communication research (social protest contests). 


## Day 1.

[Lecturer Lena and materials](https://lena-voita.github.io/nlp_course)

bag of words
neural network
[convolution filterr](https://www.ibm.com/topics/convolutional-neural-networks) This IBM webpage gives pretty good and intutitive introduction of convolutional neural network. 

[Unsupervised sentiment neuron](https://openai.com/research/unsupervised-sentiment-neuron) OpenAI 2017 paper

