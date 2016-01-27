# reddit-corpus-browser

A web interface for browsing the public reddit corpus.

**TODO:** the project currently relies heavily upon a postgres database loaded up with the corpus. I have to add scripts to take
the publicly-released corpus (a collection of JSON files) and transform it/insert it into a postgres DB. The corpus with indices
currently consumes 600GB+ of space on my instance, and may consume more as I discover the need for more indexing/refactoring into
new tables.
