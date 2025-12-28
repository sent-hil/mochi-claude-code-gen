import os
import requests
from typing import Optional, List


class MochiClient:
    """Simple client wrapper for Mochi Cards API."""

    BASE_URL = "https://app.mochi.cards/api"

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize Mochi client.

        Args:
            api_key: Mochi API key. If not provided, reads from MOCHI_API_KEY env var.
        """
        self.api_key = api_key or os.getenv("MOCHI_API_KEY")
        if not self.api_key:
            raise ValueError("MOCHI_API_KEY not found. Set it as environment variable or pass to constructor.")

        self.session = requests.Session()
        self.session.auth = (self.api_key, "")

    def create_card(
        self,
        content: str,
        deck_id: str,
        template_id: Optional[str] = None,
        tags: Optional[List[str]] = None,
        archived: bool = False,
        review_reverse: bool = False,
        pos: Optional[str] = None
    ) -> dict:
        """
        Create a new card in Mochi.

        Args:
            content: The markdown content of the card
            deck_id: The deck ID where the card should be created
            template_id: Optional template ID to apply
            tags: Optional list of tags
            archived: Whether the card should be archived
            review_reverse: Whether to enable reverse review
            pos: Position in the deck

        Returns:
            dict: The created card object

        Raises:
            requests.HTTPError: If the API request fails
        """
        url = f"{self.BASE_URL}/cards/"

        payload = {
            "content": content,
            "deck-id": deck_id
        }

        if template_id:
            payload["template-id"] = template_id
        if tags:
            payload["manual-tags"] = tags
        if archived:
            payload["archived?"] = archived
        if review_reverse:
            payload["review-reverse?"] = review_reverse
        if pos:
            payload["pos"] = pos

        response = self.session.post(url, json=payload)
        response.raise_for_status()

        return response.json()

    def get_decks(self) -> List[dict]:
        """
        Get all decks.

        Returns:
            List[dict]: List of deck objects
        """
        url = f"{self.BASE_URL}/decks/"
        response = self.session.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get('docs', [])


if __name__ == "__main__":
    # Example usage
    client = MochiClient()

    # List decks to get deck IDs
    decks = client.get_decks()
    print("Available decks:")
    for deck in decks:
        archived = " (archived)" if deck.get('archived?') else ""
        parent = f" [parent: {deck.get('parent-id')}]" if deck.get('parent-id') else ""
        print(f"  - {deck.get('name')}: {deck.get('id')}{archived}{parent}")

    # Example: Create a card
    # card = client.create_card(
    #     content="What is Python?\n---\nA high-level programming language",
    #     deck_id="your-deck-id-here",
    #     tags=["python", "programming"]
    # )
    # print(f"Created card: {card}")
