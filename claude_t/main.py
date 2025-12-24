import anthropic


client = anthropic.Anthropic(
    base_url="https://relay01.yhlxj.com", 
    api_key="sk-ant-sid01--7493a5c8fc297f48d90d9f2887918cbee681f5aa2f440d5dc5e5c5d3cf97b952"
)

response = client.beta.messages.create(
    model="claude-sonnet-4-20250514",  # or another compatible model
    max_tokens=1024,
    tools=[
        {
          "type": "computer_20250124",
          "name": "computer",
          "display_width_px": 1024,
          "display_height_px": 768,
          "display_number": 1,
        },
        {
          "type": "text_editor_20250124",
          "name": "str_replace_editor"
        },
        {
          "type": "bash_20250124",
          "name": "bash"
        }
    ],
    messages=[{"role": "user", "content": "Save a picture of a cat to my desktop."}],
    betas=["computer-use-2025-01-24"]
)
print(response)
