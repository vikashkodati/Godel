(define (triple-rule-0)
  (ground "$be" "be")
  (set-link-type "$prep" "preposition")
  (if match-rule? '((_subj $be $var0) (_obj $be $var1) ($prep $var1 $var2))
      (rule-applied "triple-rule-0")
  )
  (reset-scope)
)
(define (triple-rule-1)
  (ground "$be" "be")
  (set-link-type "$prep" "preposition")
  (if match-rule? '((_subj $be $var0) (_obj $be $var1), ($prep $var0 $var2))
      (rule-applied "triple-rule-1")
  )
  (reset-scope)
)
(define (triple-rule-2)
  (set-link-type "$prep" "preposition")
  (if match-rule? '((_predadj $var1 $var0) ($prep $var1 $var2))
      (rule-applied "triple-rule-2")
  )
  (reset-scope)
)
(define (triple-rule-4)
  (set-link-type "$in_sent" "sentence")
  (if match-rule? '((_obj $in_sent $var1) (_iobj $in_sent $var2))
      (rule-applied "triple-rule-4")
  )
  (reset-scope)
)
(define (triple-rule-6)
  (ground "$be" "be")
  (if match-rule? '((_subj $be $var1) (_obj $be $var2))
      (rule-applied "triple-rule-6")
  )
  (reset-scope)
)
(define (run-all)
  (triple-rule-0)
  (triple-rule-1)
  (triple-rule-2)
  (triple-rule-4)
  (triple-rule-6)

)
(run-all)
