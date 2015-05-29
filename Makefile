FSUFFIX = 999
LRCFOLDER = ./lrc
GRAMSFOLDER = ./grams
BINFOLDER = ./lrcParse
BAYESFOLDER = ./bayes

CUT = $(BINFOLDER)/lrc_cut.py
NGRAM = $(BINFOLDER)/main.py ngram
LRC_BAYES = $(BINFOLDER)/lrc_bayes.py

LRC = $(LRCFOLDER)/lrc$(FSUFFIX).json
LRC_JUMAN = $(LRCFOLDER)/lrc$(FSUFFIX)_cut_juman.json
NGRAMS = $(GRAMSFOLDER)/1gm-lrc $(GRAMSFOLDER)/2gm-lrc $(GRAMSFOLDER)/3gm-lrc $(GRAMSFOLDER)/4gm-lrc
NGRAMS_TOPN = 2000
BAYES_OUT = $(BAYESFOLDER)/bayes-1000
BAYES_OUTN = $(BAYESFOLDER)/1gram-1000 $(BAYESFOLDER)/2gram-1000 $(BAYESFOLDER)/3gram-1000 $(BAYESFOLDER)/4gram-1000    



juman : $(LRC_JUMAN)
$(LRC_JUMAN) : $(LRC)
	echo "LRC Cutting..."
	$(CUT) $(LRC) $(LRC_JUMAN)

ngrams : $(NGRAMS)
$(GRAMSFOLDER)/%gm-lrc : $(LRC_JUMAN)
	echo "Generating $* Grams..."
	$(NGRAM) $^ $* $(NGRAMS_TOPN) > $@

bayes : $(BAYES_OUT)
$(BAYES_OUT) : $(BAYES_OUTN)
	echo "Merging Outputs..."
	bash -c "sort $^ -r -n -t $$'\t' -k 2 -o $@"

$(BAYESFOLDER)/%gram-1000 : $(GRAMSFOLDER)/%gm-lrc $(GRAMSFOLDER)/%gm-1000
	mkdir -p $(BAYESFOLDER)
	$(LRC_BAYES) $+ > $@

clean:
	rm -rf $(BAYESFOLDER) $(LRC_JUMAN) $(NGRAMS)
