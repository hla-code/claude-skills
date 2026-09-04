# Expected Evaluation Behavior: Power BI Forecasting Handoff

## Benchmark Criteria

1. **Compliant Input (input-good.md)**:
   - Status: READY_FOR_PRODUCTION
   - Validates Star schema, dedicated DimDate, and clean 1-to-many relationships
   - Confirms proper DAX variable usage and dynamic RLS configuration

2. **Risky Input (input-risky.md)**:
   - Status: ACTION_REQUIRED
   - Flags flat-table anti-pattern and bi-directional relationship ambiguity
   - Flags dangerous raw division / without DIVIDE() error handling
   - Detects FILTER(ALL(MasterDump)) unindexed full-table scan crashing performance on 15M rows
   - Flags missing RLS and unpartitioned full refresh
   - Provides optimized DAX refactoring and Star-schema redesign plan
