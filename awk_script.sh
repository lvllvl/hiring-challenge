#!/bin/bash

awk -F'\\|' '
  !/^#/ {
    # Trim whitespace around fields
    for (i=1; i<=NF; i++) {
      gsub(/^ +| +$/, "", $i)
    }

    if ($3 == "Mars" && $4 == "Completed") {
      duration = $6 + 0  # force numeric
      if (duration > max_duration) {
        max_duration = duration
        code = $8
      }
    }
  }
  END { print code }
' space_missions.log
