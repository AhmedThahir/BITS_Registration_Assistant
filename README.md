# BITS Registration Assistant

## Requirement

```mermaid
sequenceDiagram

actor User
participant um as Upload Module
participant f as Filters
participant b as Backend

User ->> um: Upload Course List PDF<br/>from Reg dept
um ->> b: Transform data into tidy format
User ->> f: Select courses-prof combination
f ->> b: Request
b ->> User: Return list of possible courses<br/>grouped by schedule
```

Sample of a list of possible courses grouped by schedule:

- M3 W1 F4 - ML, FDS, NLP
- M2 W7 F1 - AI
- M8 T1 W1 - Blockchain, Robotics

  ...

## Suggest Toolset for Prototype

|                      |                                                              |
| -------------------- | ------------------------------------------------------------ |
| Programming Language | Python                                                       |
| Dashboard            | Streamlit                                                    |
| Data Processing      | (in order of preference)<br />1. Polars<br />2. Pandas<br />3. DuckDB |
| Visualization        | Plotly                                                       |

