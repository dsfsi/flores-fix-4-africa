# FLORES Dataset Corrections for Four African Languages

This project focuses on correcting the FLORES evaluation dataset (dev and devtest) for four African languages: **Hausa**, **Northern Sotho (Sepedi)**, **Xitsonga**, and **isiZulu**. The original dataset, though groundbreaking in covering low-resource languages, contained several inconsistencies and inaccuracies in these languages, which could affect the quality of evaluations in Natural Language Processing (NLP) tasks, especially for machine translation.

## Overview

In this project, native speakers meticulously reviewed and corrected the dataset to ensure improved accuracy and reliability for each language. Our goal was to enhance the integrity of downstream NLP tasks that use this data.

### What We Did:
1. **Reviewed and Corrected Errors**: Identified and implemented corrections to translation inconsistencies and inaccuracies in the dataset.
2. **Statistical Analysis**: Conducted statistical comparisons between the original and corrected datasets, highlighting the differences and improvements made.
3. **Improved Dataset Quality**: Enhanced linguistic accuracy and reliability, ensuring more effective evaluation of NLP tasks involving these languages.

### Key Corrections:
- **Hausa**: The Hausa translations revealed numerous inconsistencies, suggesting a significant portion may have been automatically generated, particularly due to unclear or incoherent phrasing. Comparisons with the Hausa FLORES dataset and Google Translate showed that many lexical choices were incorrect and aligned with Google’s outputs, raising concerns about the quality of the original translations. Additional issues included improper translations of named entities and the frequent omission of special characters in standardized Hausa alphabets.
- **Northern Sotho (Sepedi)**: The translations in Northern Sotho displayed a need for improvement in vocabulary consistency, syntax, and the accurate conveyance of technical terms. While most text was accurately translated, minor corrections were necessary to enhance clarity, including adjustments for borrowed words and proper spacing. Notably, some translations omitted important terms, affecting the overall meaning, such as leaving out “scientific” when referring to tools.
- **Xitsonga**: In Xitsonga translations, several vocabulary accuracy issues and improper use of borrowed terms were identified, leading to misunderstandings. Errors included incorrect translations for phrases like "Type 1 diabetes" and uniform translations lacking contextual variation, which hindered clarity. Spelling errors and the inappropriate borrowing of terms significantly impacted translation quality, underscoring the need for proper native language usage.
- **isiZulu**: IsiZulu translations faced challenges with vocabulary inconsistencies, syntax errors, and issues in expressing technical terms, compounded by the language's agglutinative structure. Key problems included incorrect grammatical structures for time expressions and the unnecessary borrowing of English terms, which disrupted linguistic flow. Efforts to standardize terminology throughout the translations were made to ensure grammatical accuracy and clarity.

### Evaluating the Corrections:

<table>
  <tr>
    <td rowspan="2">
      lang.
    </td>
    <td colspan="5">
      dev (997 sentences)
    </td>
    <td>
    </td>
    <td colspan="5">
      devtest (1,012 sentences)
    </td>
  </tr>
  <tr>
    <td>#corr. (%)</td>
    <td>#tokens<sub>o</sub></td>
    <td>#tokens<sub>c</sub></td>
    <td>&Delta; tokens</td>
    <td>% div.</td>
    <td>
    </td>
    <td>#corr. (%)</td>
    <td>#tokens<sub>o</sub></td>
    <td>#tokens<sub>c</sub></td>
    <td>&Delta; tokens</td>
    <td>% div.</td>
  </tr>
  <tr>
    <td>hau</td>
    <td>632 (63.4)</td>
    <td>17,948</td>
    <td>18,073</td>
    <td>125</td>
    <td>24.7</td>
    <td></td>
    <td>70 (6.9)</td>
    <td>2,006</td>
    <td>1,978</td>
    <td>28</td>
    <td>49.2</td>
  </tr>
  <tr>
    <td>nso</td>
    <td>67 (6.7)</td>
    <td>2,226</td>
    <td>2,271</td>
    <td>45</td>
    <td>28.9</td>
    <td></td>
    <td>62 (6.1)</td>
    <td>2,082</td>
    <td>2,105</td>
    <td>23</td>
    <td>28.0</td>
  </tr>
  <tr>
    <td>tso</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td></td>
    <td>83 (6.1)</td>
    <td>2,919</td>
    <td>2,947</td>
    <td>28</td>
    <td>27.4</td>
  </tr>
  <tr>
    <td>zul</td>
    <td>190 (19.1)</td>
    <td>3,605</td>
    <td>3,588</td>
    <td>17</td>
    <td>23.7</td>
    <td></td>
    <td>226 (22.3)</td>
    <td>4,414</td>
    <td>4,396</td>
    <td>18</td>
    <td>31.8</td>
  </tr>
</table>

**Table:** Data statistics; #corr. (%) → number of sentences requiring at least one correction (percentage of original data); #tokens<sub>o</sub> → original token count; #tokens<sub>c</sub> → corrected token count; &Delta; tokens → token count difference; % div. → percentage of token divergence.

<table>
  <tr>
    <td rowspan="3">
      lang.
    </td>
    <td colspan="4">
      dev
    </td>
    <td>
    </td>
    <td colspan="4">
      devtest
    </td>
  </tr>
  <tr>
    <td colspan="2">TER</td>
    <td rowspan="2">BLEU</td>
    <td rowspan="2">COMET</td>
    <td></td>
    <td colspan="2">TER</td>
    <td rowspan="2">BLEU</td>
    <td rowspan="2">COMET</td>
  </tr>
  <tr>
    <td>Score</td>
    <td>#Edits</td>
    <td></td>
    <td>Score</td>
    <td>#Edits</td>
  </tr>
  <tr>
    <td>hau</td>
    <td>19.2</td>
    <td>3,107</td>
    <td>72.0</td>
    <td>54.1</td>
    <td></td>
    <td>40.4</td>
    <td>711</td>
    <td>56.6</td>
    <td>42.1</td>
  </tr>
  <tr>
    <td>nso</td>
    <td>22.4</td>
    <td>472</td>
    <td>68.5</td>
    <td>55.2</td>
    <td></td>
    <td>21.2</td>
    <td>409</td>
    <td>71.8</td>
    <td>55.9</td>
  </tr>
  <tr>
    <td>tso</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td></td>
    <td>20.9</td>
    <td>547</td>
    <td>73.9</td>
    <td>58.4</td>
  </tr>
  <tr>
    <td>zul</td>
    <td>17.2</td>
    <td>524</td>
    <td>76.3</td>
    <td>53.0</td>
    <td></td>
    <td>23.6</td>
    <td>879</td>
    <td>70.6</td>
    <td>53.0</td>
  </tr>
</table>

**Table:** Similarities between the original and corrected FLORES evaluation data on the four African languages - original as predictions; corrected as reference translations.

## How to Use

This repository contains the corrected version of the FLORES dataset for the four languages. You can use these corrected datasets for improved performance in evaluating machine translation and other NLP tasks for African languages.

### Accessing the Data
- [Download corrected datasets](https://github.com/dsfsi/flores-fix-4-africa/tree/main/data/corrected)

## Contributing

We welcome contributions and suggestions to further enhance the dataset. If you would like to contribute, please submit a pull request or open an issue.

## Acknowledgments

Special thanks to the native speaker annotators—university students and researchers—who volunteered to correct translations in their native languages. Their valuable contributions are crucial to the development and preservation of these low-resource languages in NLP.

## Citation

If you use these corrections in your research, please cite our paper:

```
@misc{abdulmumin2024correctingfloresevaluationdataset,
  title={Correcting FLORES Evaluation Dataset for Four African Languages}, 
  author={Idris Abdulmumin and Sthembiso Mkhwanazi and Mahlatse S. Mbooi and Shamsuddeen Hassan Muhammad and Ibrahim Said Ahmad and Neo Putini and Miehleketo Mathebula and Matimba Shingange and Tajuddeen Gwadabe and Vukosi Marivate},
  year={2024},
  eprint={2409.00626},
  archivePrefix={arXiv},
  primaryClass={cs.CL},
  url={https://arxiv.org/abs/2409.00626}, 
}
```

---

We hope these corrections will improve your NLP research and contribute to the growing body of work on African languages!