# med-abbrev-mystery

Electronic Health Records (EHRs) are a critical data source for Natural Language Processing (NLP) applications in healthcare. Despite their utility, the widespread use of abbreviations in EHRs can lead to misinterpretations and re- duced clarity, posing challenges for clinical de- cision making. This study aims to improve the interpretation of medical abbreviations in clinical texts by fine-tuning Bidirectional Encoder Representations from Transformers (BERT) models using the Medical Dataset for Abbre- viation Disambiguation for Natural Language Understanding (MeDAL), crafted by Wen et al. (2020) containing 5,886 abbreviations with approximately 4 expansions on average for each. The abbreviations come from 14,393,619 medical abstracts on PubMed. The fine-tuned BERT models were applied to two medical tasks: mor- tality prediction and diagnosis prediction. We hypothesize that fine-tuning on medical abbreviations will enhance the models’ ability to process clinical text and improve task performance, and that performance improvements can be obtained by fine-tuning Large Language Models (LLMs) on the abbreviation disambiguation task. Results were mixed with some indication that fine-tuning BERT models on abbreviation disambiguation does offer modest performance improvements on downstream mortality and diagnosis prediction tasks in line with those observed in Wen et al. (2020) but we ultimately conclude that there is more exploration which can be done in fine-tuning BERT models on medical abbreviations to improve downstream task performance.

Check out 266_Final_Paper.pdf for a paper describing our work and accomplishments.
