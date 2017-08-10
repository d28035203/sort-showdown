# Sort Showdown

Side-by-side comparison of bubble, insertion, quicksort, and mergesort on the same array. Reports wall time and comparison counts.

## Run

```bash
python3 showdown.py
python3 showdown.py -n 200
python3 showdown.py -n 50 --reverse
python3 showdown.py -n 50 --sorted
```

## Notes

- Comparison counts are approximate instrumentation, not formal big-O proofs.
- Quicksort uses a simple last-element pivot (worst case on sorted input).
- Good demo for algorithm lab write-ups and complexity intuition.

## License

MIT
