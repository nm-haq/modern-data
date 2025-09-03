Project Title
Modern Retail Sales Dashboard (Power BI)

Executive Summary
This repository contains a Power BI dashboard that analyzes sales performance for a Malaysian retail dataset. The report focuses on high-level KPIs, time-series trends, segment comparisons, and sales mix, enabling quick insight into total sales, seasonality, and top/bottom performing segments. It is designed for weekly operational reviews and executive decision-making.

Problem Statement
Retail leaders need a unified, interactive view of sales to:
- Monitor total sales and growth over time
- Identify top and underperforming categories/regions
- Understand sales concentration risk and product mix
- Drill into segments quickly to guide inventory, pricing, and marketing actions

Dataset Source
- Primary table: malaysian_retail_store
- Core measure: Sum(malaysian_retail_store.TotalAmount)
- Data scope: Retail transactions aggregated for sales analysis
Note: The PBIX encapsulates the model; if you need the raw source files or a CSV export, I can extract and include them.

Methodology
- Data modeling: Sales facts modeled around TotalAmount with categorical dimensions (e.g., category, region) and time.
- Visual design:
  - KPI cards for headline sales metrics
  - Line chart for time-series trend analysis (seasonality and growth)
  - Clustered bar/column charts for segment comparisons
  - Pie chart for sales mix and concentration
  - Slicer for interactive filtering (e.g., period, region, product group)
- Interaction: Cross-filtering enabled to explore segments and time windows coherently.

Result
- A single-page Power BI dashboard that:
  - Surfaces total sales via KPI cards
  - Reveals trends and seasonal patterns with a line chart
  - Highlights top and bottom segments with bar/column visuals
  - Shows sales concentration via a pie chart
  - Supports quick slice-and-dice analysis with a global slicer
Outcomes: Faster decision cycles, clearer prioritization of segments, and better-timed campaigns and inventory allocation.

The Functioning of BI Dashboard
- Page layout:
  - KPI Cards: Display total sales and key headline metrics.
  - Line Chart: Shows sales over time for trend and seasonality.
  - Clustered Bar/Column Charts: Compare sales across categories, regions, or other segments.
  - Pie Chart: Displays sales mix distribution across segments.
  - Slicer: Filters the entire page using a key dimension for rapid comparative analysis.
- Typical workflows:
  - Weekly ops: Filter by latest week/month, review top segments, spot trend shifts.
  - Merchandising: Identify lagging categories and test price/assortment adjustments.
  - Marketing: Align campaigns with peak periods and diversify if sales are concentrated.

Acknowledgement:
I would like to acknowledge the contributions of the open-source community and the developers of Pandas and Matplotlib, whose powerful libraries made this analysis possible.

Special thanks to the academic instructors and peers who provided guidance and feedback during the course project. Their insights helped shape the business questions and analysis framework.

Finally, appreciation goes to the sources of the retail dataset, which enabled practical exploration of real-world business problems through data analysis.
