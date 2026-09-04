# DAX Best Practices Reference

## Performance Optimization Rules
1. **Filter Context Efficiency**: Avoid FILTER(all(Table), ...) when KEEPFILTERS() or CALCULATE(..., Table[Column] =  Value) can be used.
2. **Context Transition**: Be mindful when using CALCULATE() inside SUMX / AVERAGEX as it triggers context transition across every row.
3. **Optimized Forecasting Measure Example**:
`dax
Forecast Upper Bound 95% = 
VAR _SelectedDate = MAX('DimDate'[Date])
VAR _CurrentTrend = [Baseline Revenue]
VAR _StdDev = [Historical Residual StdDev]
RETURN
    IF(
        _SelectedDate > [Max Actual Date],
        _CurrentTrend + (1.96 * _StdDev * SQRT([Forecast Horizon Step])),
        BLANK()
    )
`
