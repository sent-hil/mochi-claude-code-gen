# Flashcards Generator

Generate flashcards from notes in the `todo/` folder following the rules in `rules/flashcard-rules.md` and the format shown in `rules/examples.md`.

## Workflow

1. Read the rules from `rules/flashcard-rules.md`
2. Read example cards from `rules/examples.md`
3. Read the input file from `todo/`
4. Generate flashcards following the rules
5. Write output to a markdown file named `{topic}-flashcards.md`

## Output Format

- Each flashcard separated by `---`
- No `---` at the beginning or end of file
- Focus on practical, actionable knowledge
- Use "How to" questions over yes/no questions
- Simple, everyday language
- Code wrapped in triple backticks with language specified
- Write to md file in `output/` folder
