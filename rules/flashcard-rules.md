* Wrap code in ```<lang>``` when providing code snippets.

Example:
```python
np.arange(6).reshape((2,3))
```

* Separate each flashcards and front and back of each flashcard with `---`.

Create a numpy array from `[1975, 1979]`.
---
```python
years = np.array([1975, 1979])
```
---

* Use simple, everyday language when asking questions

* Prefer "How to" questions over yes/no questions. Put setup/context in the question, and keep the answer focused on the solution.

Example (Good):
How to combine two lists?
```ruby
list_one = [1, 2]
list_two = [3, 4]
```
---
```ruby
[*list_one, *list_two]
```

Example (Avoid):
Does `[*list_one, *list_two]` work in Ruby?
---
Yes! It works the same way as Python for arrays.

* Avoid superficial trivia questions. Focus on practical, actionable knowledge. Don't create cards about version numbers, release dates, or historical facts unless critical to understanding.

Example (Avoid):
When was hash unpacking with `**` introduced in Ruby?
---
Ruby 2.0+

Example (Good):
How do you unpack a hash into keyword arguments?
[practical code example]

* Do not include a --- at the very beginning or very end of the file.
