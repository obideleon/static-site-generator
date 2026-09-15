import unittest

from markdown_blocks import BlockType, block_to_block_type, markdown_to_blocks


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.ULIST)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.OLIST)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_block_type_all(self):
        md = """
# Welcome to Python 3 Regex Challenge

> Test
>asd

## This is the first header tag

```
for i in range(0, 10):
    print(f"Printing #{i + 1}")
```

## This is the second header tag

- Test 1
- Test 2
- Test 3

## This is the third header tag

1. Open Code Editor
2. Make a new feature or changes
3. Commit the changes

That's all!
"""
        blocks = markdown_to_blocks(md)
        blocks_type = []
        for block in blocks:
            blocks_type.append(block_to_block_type(block))
        self.assertListEqual(blocks_type, [
            BlockType.HEADING,
            BlockType.QUOTE,
            BlockType.HEADING,
            BlockType.CODE,
            BlockType.HEADING,
            BlockType.ULIST,
            BlockType.HEADING,
            BlockType.OLIST,
            BlockType.PARAGRAPH
        ])


if __name__ == "__main__":
    unittest.main()
