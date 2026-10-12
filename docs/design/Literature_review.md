# Literature Review

This review covers regular expressions and finite-state transducers for information extraction and normalization from resumes. Person B's topics (automata for classification, grammars and DSLs) are not covered here.

## Regular expressions and text normalization

Regular expressions describe the regular languages, and they are the usual first tool for finding patterns in text. Jurafsky and Martin's textbook introduces them together with text normalization, the step that turns the many written forms of the same item into one standard form. This is what ResumeLens does in its first two stages: ten regular expressions find the data, and the normalization stage maps variants such as `JS`, `Javascript` and `JavaScript` to a single label.

Zupon, Crew and Ritchie (2021) show a case where normalization is built with finite-state transducers. They built a text normalizer with Pynini, a Python library for finite-state transducers, and studied how normalization and data quality affect language models for eight low-resource African languages. Their setting is different from ours (language modeling, not resumes), but the tool choice is the same: a transducer is a natural way to write normalization rules, and Python libraries make it practical.

## Finite-state transducers in resume processing

Guo, Alamudun and Hammond (2016) present RésuMatcher, a résumé-job matching system. According to the article, it uses a finite-state transducer based tool to extract qualifications and experience from résumés and requirements from job postings, builds a technical skills dictionary automatically, and ranks jobs with a statistical similarity index. It is the closest work to ours because it also applies transducers to resumes. The difference is the role of the transducer: in RésuMatcher it performs the extraction itself, while in ResumeLens the extraction uses regular expressions and the transducers only normalize what was extracted.

## Rule-based information extraction from resumes

Amdouni and Karaa (2010) start from the problem that e-recruitment receives a growing number of CVs in different formats, so automated techniques are needed to extract and use their information. They analyze CVs written in French by extending GATE (a text-engineering framework) with hand-written rules, and they normalize the content to the Europass CV structure, guided by the HR-XML standard. They report an improvement in the extraction phase. Like ResumeLens, they combine extraction rules with a normalization target, although their target is a document structure and ours is a closed vocabulary of skills.

Musleh (2024) uses Python regular expressions to extract eight fields (name, date of birth, email, phone, GPA, gender, nationality and address) from resumes, and reports 96.4% precision on the test set (25 resumes from a private corpus of 75). The author points out two limits that also apply to us: the approach is sensitive to large changes in resume format, and it only handles English.

Chen, Zhang and Niu (2018) propose a two-step algorithm for extracting information from resumes, which shows that resume processing is often split into stages instead of done in one pass, as ResumeLens does.

## Statistical and hybrid approaches

Vukadin et al. (2021) extract information from free-form CVs in several languages with learned models, which gives more flexibility than rules when the layout and the vocabulary vary. Wosiak (2021) combines dictionary methods with named-entity recognition tools for Polish IT resumes, a hybrid that keeps a dictionary of known skills and adds a learned component.

## Positioning of ResumeLens

| Aspect | Typical rule-based work (Musleh, 2024; Amdouni & Karaa, 2010) | ResumeLens (Person A) |
|--------|--------------------------------------------------------------|-----------------------|
| Target fields | Personal data, or the sections of the CV | Personal data plus technical skills (languages, frameworks, databases, tools, other qualifications), years of experience and academic degrees |
| Role of finite-state transducers | Not used (Musleh) or not reported | Normalization of skills (RésuMatcher uses transducers for extraction instead) |
| Normalization | Matched text, or a document structure (Europass) | Canonical labels from a closed vocabulary |
| Formal specification | Rules or regular expressions listed | Regular expressions and 7-tuple transducers with diagrams |
| Ordering | Not addressed | Canonical order per target profile |
| Evaluation | Precision on a private corpus | Unit tests over four reference resumes plus documented edge cases |
| Limits | Format-sensitive, one language | Same, plus a fixed vocabulary (new skills need new patterns and transitions) |

Gap addressed. The works above either extract fields without normalizing them, normalize to a document structure, or use transducers for extraction. ResumeLens separates the two jobs: regular expressions extract, transducers normalize skills to canonical labels, and a canonical order per profile prepares the list for the automata and the DSL of the next stages.

Limits. The vocabulary is closed, so unknown skills are ignored. The patterns are case-sensitive and biased to ASCII letters (see limitations L1 to L6 in the formalization document), and the evaluation set is small. Learning-based approaches (Vukadin et al., 2021; Wosiak, 2021) would be the natural extension for an open vocabulary.

## References

* Amdouni, S., & Ben abdessalem Karaa, W. (2010). Web-based recruiting. *ACS/IEEE International Conference on Computer Systems and Applications - AICCSA 2010*, 1–7. https://doi.org/10.1109/AICCSA.2010.5587018
* Chen, J., Zhang, C., & Niu, Z. (2018). A two-step resume information extraction algorithm. *Mathematical Problems in Engineering, 2018*, 5761287. https://doi.org/10.1155/2018/5761287
* Guo, S., Alamudun, F., & Hammond, T. (2016). RésuMatcher: A personalized résumé-job matching system. *Expert Systems with Applications, 60*, 169–182. https://doi.org/10.1016/j.eswa.2016.04.013
* Jurafsky, D., & Martin, J. H. *Speech and Language Processing* (3rd ed. draft). Chapters on regular expressions and text normalization. https://web.stanford.edu/~jurafsky/slp3/
* Musleh, D. A. (2024). Rule-based information extraction from multi-format resumes for automated classification. *Mathematical Modelling of Engineering Problems, 11*(4), 1044–1052. https://doi.org/10.18280/mmep.110422
* Vukadin, D., Kurdija, A. S., Delač, G., & Šilić, M. (2021). Information extraction from free-form CV documents in multiple languages. *IEEE Access, 9*, 84559–84575. https://doi.org/10.1109/ACCESS.2021.3087913
* Wosiak, A. (2021). Automated extraction of information from Polish resume documents in the IT recruitment process. *Procedia Computer Science, 192*, 2432–2439. https://doi.org/10.1016/j.procs.2021.09.012
* Zupon, A., Crew, E., & Ritchie, S. (2021). Text normalization for low-resource languages of Africa. *arXiv*. https://doi.org/10.48550/arXiv.2103.15845