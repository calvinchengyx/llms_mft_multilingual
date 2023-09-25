# Oxford LLMs Workshop Notes
All notes are from the [Oxford LLMs workshop](https://www.llmsforsocialsciene.dev/) held on Sep 27-29, 2023. Thanks to [Maksim Zubok](https://www.llmsforsocialsciene.dev/posts/people/) for organizing. 

## Day -1. Preparation (Sep 25)
### Tasks 
1. ~~Create a GitHub page to make notes of the workshop and store codes~~
2. civic_j project summary
3. Clean-up civic_j codes, make it ready for open-repo
4. Get ready for your moral foundation paper, set the goal, draft the research design, and make a to-do list this week 
5. Go through python tutorial in the workshop page 

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
* __LLMs(ChatGPT)__: GPT-3.5-turbo, curie, adas 

