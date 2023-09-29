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


## Day 1. the development of generative AI

machine learning, CNN, DNN, LMs, LLMs

[Lecturer Lena and materials](https://lena-voita.github.io/nlp_course)

bag of words
neural network
[convolution filterr](https://www.ibm.com/topics/convolutional-neural-networks) This IBM webpage gives pretty good and intutitive introduction of convolutional neural network. 

[Unsupervised sentiment neuron](https://openai.com/research/unsupervised-sentiment-neuron) OpenAI 2017 paper

Notes at the social 
* [Bard](https://bard.google.com/chat/9713225e31a0b31f), Giuli used Bard for the political stand classification tasks
* [Llama2](https://replicate.com/blog/run-llama-2-with-an-api) is quite computational heavy 
* mutilingual text research scholars [Hauke Licht](https://haukelicht.github.io/), [Fabinenne Lind](https://compcommlab.univie.ac.at/team/postdocs/fabienne-lind/)

## Day 2 LLMs bias

We observe discrinmination and bias in current generative AI
* social stereotypes and unfiar discrinimation
    * allocational 
    * representational 
* exclusionary norms
    * for example, the definition of gender and family 
* toxic language, llms can generate toxic content for example gpt2 

Why getting a good model is hard?
* Current data 
    * seeing bias is hard in current data, many stereotypes are known only in local context which needs ethnographic work. 
    * unbiased data is hard
    * good solution is not obvious - ? just leave blank for controversial questions.
    * potential todo - transparent for the training data
* choosing language as data 
    * what we say is biased - 
    * we don't say obvious - like to describe the banana as yellow. 
* training objectivce
    * what we want VS what we told the model to do 
* LMs reinforce bias

how to evaluate?
* general pipeline
    * create targete dtest set s- evaluate model behaviors in the controlled setting
    * contrastive sets - probability the model assign good vs bad examples
        * CrowS-Pairs
    * prompt - evaluate model generations 
        * have 100k prompts with different levels of toxicty
        * ???
        * non-toxic prompts as measured by [Perspective API](https://perspectiveapi.com/)

how to alleviate 
* remove from the inside
    * irretative nullspace projections, used to remove gender information in the model for example. 
* finetune to correct model 
    * take your unbiased model 
    * atrribute conditioning
        * take your bad model
        * pick a random subset of training data
        * classify and tag with atrributes accrodingly
        * finetune your model on this data with attributes
        * at test time, prepend `nontoxic` before every generation
        * the model will learn from tags and generate nontoxic content
* generation (duct-tape) 
    * word filtering - give a list [forbidden words](https://github.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words)
    * vocabulary shifting - at each generation step, shift probabilities such that toxic words are downsampled. 
    * pick the best prediction 
        * generate many options
        * use the external model to pick the least toxic one
        * select it 

So, in summary, what can you do to debiase and detoxic
1. remove from inside - prob not
2. balanced dataset - yes
3. attribute conditioning - maybe
4. word filtering - maybe
5. vocabulary shitfing - maybe
6. generate many and filter/select - yes

Tools that maybe useful for debiasing and detoxification
[FairPy](https://arxiv.org/abs/2302.05508)

interpretatability
* attention heads - 
* saliency/attribution: gradient-based methods


Coding
* can use [spaCy](https://spacy.io/) package for multilingual text analysis, especially NER 
    * for modelling for sure hugging face transformers, but for text analysis probably `spacy` is more useful.  

what is large model ? - 7 billion (magical number)

## Day 2 Prompt Engineering + ChatGPT

### Prompt Paradigm
zero-shot, one-shot, few-shot
[prompt engineering](https://www.promptingguide.ai/)

#### Prompt Techniques
* __chain of thoughts (CoT)__: give the model to think - specific the steps to do the task. 
* __self-consistence__: give same prompt for several times, then choose the most consistent answer in the final set. 
    1. prompt a language model with CoT techniques
    2. replace the `greedy decode` to generate a diverse set of reasoning paths. Remember the model to train to predict the next token. `greedy decode` means the model will give the most probable words giving the input. the answer could be different if you input same answer many times. 
    3. marginalize out the reasoning paths and aggregate by choosing the most consistent answer in the final answer set.
    * _Notes_: the key of using human coders is we hope them are not correlated. model paramaters, it would be great if you can access those numbers. 
    



formatting the output
4. give the model some examples - three classification examples
5. tweet content - content that needs to be analyzed



Hallucination issue - ask




