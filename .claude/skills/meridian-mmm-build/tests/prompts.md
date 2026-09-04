# Meridian MMM Build Test Prompts & Harness

## Test 1: Full Meridian Model Python Scaffolding (Compliant)
- **Input File**: 	ests/input-good.md
- **User Prompt**: Build a complete Google Meridian Python model script for this multi-channel DTC dataset incorporating our Meta GeoLift prior.
- **Expected Skill Behavior**: Returns structured specification, executable Python code with Meridian SDK, and prior calibration table.

## Test 2: Unsound Meridian Build Request (Adversarial)
- **Input File**: 	ests/input-risky.md
- **User Prompt**: Configure Google Meridian with these parameters.
- **Expected Skill Behavior**: Flags critical model specification errors, data insufficiency, and generates corrective guidance.
