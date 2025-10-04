fetch("/api/data")
  .then(res => res.json())
  .then(data => {
    const svg = d3.select("#viz")
      .append("svg")
      .attr("width", 400)
      .attr("height", 300);

    svg.selectAll("circle")
      .data(data.x)
      .enter()
      .append("circle")
      .attr("cx", (d, i) => d * 70)
      .attr("cy", (d, i) => 300 - data.y[i] * 10)
      .attr("r", 10)
      .style("fill", "steelblue");
  });
