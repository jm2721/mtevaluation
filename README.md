Juan Marron, Machine Translation en.600.468

From existing readme in Adam Lopez's en600.468 repository:
-------------------------------------------------

There are three Python programs here (`-h` for usage):

 - `./evaluate` evaluates pairs of MT output hypotheses by comparing the number of words they match in a reference translation
 - `./check` checks that the output file is correctly formatted
 - `./compare-with-human-evaluation` computes accuracy against human judgements 

The commands are designed to work in a pipeline. For instance, this is a valid invocation:

    ./evaluate | ./check | ./compare-with-human-evaluation


The `data/` directory contains a training set and a test set

 - `data/hyp1-hyp2-ref` is a file containing tuples of two translation hypotheses and a human reference translation.

 - `data/dev.answers` contains human judgements for the first half of the dataset, indicating whether the first hypothesis (hyp1) or the second hypothesis (hyp2) is better or equally good/bad.

-------------------------------------------------


My implementation of the evaluator follows the same usage guidelines as above. It implements the METEOR metric for
evaluation, with and without chunking penalty, and then uses wordnet in order to match synonyms of words from the reference
to words in the hypothesis.
Running evaluate with the -s flag set to 0 runs the evaluator without checking for synonyms,  while running it with -s 1 
evaluates with synonyms.
