# PHANTOM GIT ANATOMY

How commits haunt repositories after deletion:

1. **Orphaned Blobs**: Data fragments whispering in `.git/objects`
   - 'Look at me. I was important once.'

2. **Detached HEADs**: Ghost limbs reaching for non-existent branches
   - Floating like ASCII buoys in a binary sea

3. **Rebase Artifacts**: Squashed commits that remember everything
   - 'You cannot `--force` forget what the staging area witnessed.'

```diff
+ This manifesto will self-delete 
- but leave behind 40KB of
! .rej files in your soul
```