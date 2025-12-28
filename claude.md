# Flashcards Generator

Generate flashcards from notes in the `todo/` folder following the rules in `rules/flashcard-rules.md` and the format shown in `rules/examples.md`.

## Workflow

1. Read the rules from `rules/flashcard-rules.md`
2. Read example cards from `rules/examples.md`
3. Read the input file from `todo/`
4. **Check for existing cards**: Search `markdown-export/` folder for similar questions to avoid duplicates
   - Look for cards with similar topics or questions
   - Compare generated questions with existing card questions
   - Flag or skip cards that are duplicates or very similar
5. Generate flashcards following the rules (excluding duplicates)
6. **Group questions into cards**: Combine multiple Q&A pairs into single cards
   - Each Mochi card can contain multiple question-answer pairs
   - Limit to **5 Q&A pairs per card maximum**
   - If more than 5 pairs exist, create multiple cards
   - Separate each Q&A pair within a card with `---`
7. Write output to a markdown file named `{topic}-flashcards.md` in `output/` folder
8. **Determine target deck**: Intelligently find the most appropriate deck
   - Get all available decks using `client.get_decks()`
   - Analyze the card content/topic (e.g., "Python", "Ruby", "ML", "Math")
   - Search for deck names that match the topic (case-insensitive)
   - Consider deck hierarchy - prefer leaf decks over parent decks
   - Exclude archived decks unless no active deck matches
   - Present the suggested deck to user for confirmation
9. **Post to Mochi**: Use `mochi_client.py` to create cards in Mochi via API
   - Import and use `MochiClient` to post each card
   - Each card's content should include multiple Q&A pairs (up to 5)
   - All Q&A pairs in a card separated by `---`
   - Report which cards were successfully created
10. **Update local export**: Save newly created cards to `markdown-export/` folder
   - Create file in appropriate deck folder hierarchy
   - Filename format: `{card-id} - {first-question-truncated}.md`
   - This keeps the local export in sync with Mochi

## Mochi API Integration

Use `mochi_client.py` to interact with Mochi:

```python
from mochi_client import MochiClient

client = MochiClient()  # Reads MOCHI_API_KEY from environment

# Get available decks
decks = client.get_decks()

# Create a card with single Q&A
card = client.create_card(
    content="Question text\n---\nAnswer text",
    deck_id="deck-id-here",
    tags=["optional", "tags"]
)

# Create a card with multiple Q&A pairs (up to 5)
card = client.create_card(
    content="Question 1\n---\nAnswer 1\n---\nQuestion 2\n---\nAnswer 2\n---\nQuestion 3\n---\nAnswer 3",
    deck_id="deck-id-here",
    tags=["optional", "tags"]
)
# Returns: {'id': 'card-id', ...}
```

Run with: `MOCHI_API_KEY=... uv run python mochi_client.py` to list decks.

## Existing Cards

The `markdown-export/` folder contains all existing Mochi cards exported in markdown format. Each file:
- Contains one or more flashcards separated by `---`
- Filename format: `{card-id} - {first-question-text}.md`
- Organized in deck hierarchy folders

When checking for duplicates:
- If the folder is empty (only .gitkeep exists), skip duplicate checking and proceed with all generated cards
- If files exist, search using grep or file reading to find similar questions
- Handle the case gracefully if no matches are found

## Output Format

- Multiple Q&A pairs grouped into single cards (max 5 pairs per card)
- Each question and answer separated by `---`
- No `---` at the beginning or end of file
- Focus on practical, actionable knowledge
- Use "How to" questions over yes/no questions
- Simple, everyday language
- Code wrapped in triple backticks with language specified
- Write to md file in `output/` folder
- Report any duplicates found and excluded

Example card with multiple Q&A pairs:
```
How do you create a list in Python?
---
```python
my_list = [1, 2, 3]
```
---
How do you append to a list?
---
```python
my_list.append(4)
```
---
How do you get list length?
---
```python
len(my_list)
```
```
