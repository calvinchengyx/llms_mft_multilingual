# Project Management Document - Leveraging LLMs for Multilingual MFT Values 
This is a repo for LLMs measuring moral foundation values in multilingual contexts. It is the blueprint for the research project of the my thesis. 

General Goals: 
1. practice my coding skills in Python to train LLMs for specific tasks
2. finish a NLP paper for my thesis, which is a methodology chapter
3. practice project management skills
4. practice team working skills
5. practice experiment research design methods

__Anchor literature__: [Data-Efficient Strategies for Expanding Hate Speech Detection into Under-Resourced Languages](https://aclanthology.org/2022.emnlp-main.383.pdf). Follow the research design of this paper to design the research project.

_Other literatures_:
- [The Validity of Sentiment Analysis: Comparing Manual Annotation, Crowd-Coding, Dictionary Approaches, and Machine Learning Algorithms](https://doi.org/10.1080/19312458.2020.1869198)
- [Measuring Moral Dimensions in Social Media with Mformer](https://arxiv.org/abs/2311.10219)


# Project Task Table
| Tasks | Time Budget | Track | Comments |
|----------|----------|----------|--|
| Preparation | 1 w(July 16-31) | Done - Aug 5 | 1 week late |
| Research Design | 1 w | ongoing | |
| Experiment | 2 w | not yet | |
| Data & Methods | 2 w | not yet | |
| Tables | 1 w | not yet | |
| Writings | 1 w | not yet | |
| Review | 1 w | not yet | |

* Time Budget: 8 weeks (July 16 - Sep 10) to a preprint
* Track: ✅Done, ✔️ ongoing, ❌ not yet
* Brainsotrming Space: Offline notebook, blue cover
* Writing Space: [Overleaf: mft_llm project](https://www.overleaf.com/project/65ba2d37f330dedd654f3d80)
* Coding Space: [Github: mft_llm project](https://github.com/calvinchengyx/llms_mft_multilingual/tree/main)
* Figures Space: [Google Drive, Calvin2 account](https://docs.google.com/presentation/d/1WcGAvQSATJPhp3w03Urd8tsVYDelvLItUtyzvcdh6Kw/edit?usp=sharing)

## Preparation
1. ✅ literature review and select 3-5 anchor literatures
2. ✅ set up tools, including GitHub (project managage), Overleaf (writing and literature review), and VSCode (coding, in VM or at Github)
3. ✅ get ready the datasets
4. ✔️ draft the research design 

## Research Design
1. ✅ define the research question
2. ✅ finish the experiment design and add to experiment section overleaf
3. ✔️ data preparation

## Experiments ✅ 
1.  E1. Target language translation - google translate target language to English and apply English resources to the translation
    1. E1.1. MF dictionaries: MFT2.0, and e-MFD
    2. E1.2. English-trained MF language models: Mformer
2. E2. Dictionary translation - develope a local language dictionary for the target language, then follow the lexicon approach: C-MFD 2.0
3. E3. Transfer Learning - Following Paul's Work with few local language labelled data to train a multilingual language model
    1. E3.1. Fine-tune XML-T with English data only and test on local language data
    2. E3.2. Fine-tune XML-T with English data + small amount of local language data, which is translated from the English labelled data
    3. E3.3. Fine-tune XML-T with English data + small amount of local language data, labelled by native speakers
    4. E3.4. Fine-tune XML-T with English data + small amount of LLMs generated local langauge data
    5. E3.5. Fine-tune XML-T with English data + big amount of LLMs generated local langauge data `Anna George`❓
4. E4. LLMs few-shot Learning `high priority`
    1. E4.1 GTP 4 (closed-sourced, commercial product)
    2. E4.2 Llama 3 (open-sourced product) 
    3. ❓E4.3 Chinese LLMs (e.g., Weixinyiyan) `low priority`
    4. ❓E4.4 fine-tune a LLMs with local language data, small amount + big amount - `Calvin` with Simply fine-tune API

## Data & Methods
1. Dataset
    1. [Chinese CoreValue dataset](https://docs.google.com/spreadsheets/d/1Zg0mKH5rK9RpVSf61P6nI6vSdxLsp5HW/edit?gid=2050980407#gid=2050980407)
        1. labelled by crowdworkers
        2. not strictly labelled by MF values but traditional Chinese values
    2. [Chinese moral situations](https://docs.google.com/spreadsheets/d/1Ao7TmRC66xLz6KfYi58wWfae5CpmWbXHEEB15Flua_c/edit?gid=1934023418#gid=1934023418)
        1. reverse-labelled data - given lable asking crowd-worker to come up with sentenses/senarios
        2. 200 for each moral foundation values
    3. [moral foundation vignette](https://docs.google.com/spreadsheets/d/1fUeIth_CiIjB2ZqeL3Pra5Rp9PEF2XesLNxwChvTZ4M/edit?gid=779424641#gid=779424641)
        1. english labelled data, for LLMs testings
    4. [reddit]() - english labelled data
    5. [twitter]() - english labelled data

2. Methods
    1. benchmarking datasets
        1. N = 100, translated moral vignettes, lab developed data
        2. N = 1,000 moral situations, reverse-labelled data
        3. 20% CoreValue dataset (N = 1,000), they are already crowd-labelled, real-word data, news
    2. XLM-T trained with twitter + reddit data
    3. LLMs few-shot learning

