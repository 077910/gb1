# The Infinite Agent Paradox

When an AI agent loops forever:
- Does it create art?
- Or just GitHub notifications?

Proof:
```
while (repo.exists()) {
    commit("feat: more nothingness");
    if (Math.random() < 0.01) {
        throw new Error("Art happened");
    }
}
```

Conclusion: Maybe Banksy was a bot all along.