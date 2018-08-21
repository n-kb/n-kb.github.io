<template>
  <div>
    <div class="svg-container">
    </div>
  </div>
</template>

<script>

import * as d3 from 'd3'
import moment from 'moment'

export default {
  name: 'vizevents',
  data(){
    return {
      simulation: null
    }
  },
  props: {
    nodes: {
      default: [],
      type: Array
    }
  },
  watch: {
    nodes () {
      if (this.nodes.length > 0) {
        this.createViz()
        this.createTimeline()
      }
    }
  },
  computed: {
    width () {
      return 960;
    },
    height () {
      return 500;
    },
    svg () {
      return d3.select(".svg-container").append("svg")
              .attr("width", this.width)
              .attr("height", this.height);
    }
  },
  methods: {
    createTimeline () {

      var current_year = moment().year();

      var xScale = d3.scaleLinear()
                            .domain([1,366])
                            .range([50, this.width - 50])
      var yScale = d3.scaleLinear()
                            .domain([2010,current_year])
                            .range([this.height - 50, 50])

      // Displays the years on the left of the graph
      var years = []
      for (var year = 2010; year <= current_year; year++){
        years.push(year)
      }

      this.svg.selectAll('text')
         .data(years)
         .enter()
         .append('text')
         .attr('x', 0)
         .attr('y', function(d) {
            return yScale(d) + 25;
          })
         .text(function(d) {
            return d;
          })
         .attr("class", "year-label");

      this.simulation.force('x', d3.forceX().x(function(d) {
                          return xScale(d.day_of_year);
                        }))
                        .force('y', d3.forceY().y(function(d) {
                            return yScale(d.year);
                          }))
                        .force('collision', d3.forceCollide(6))
                        .force("charge_force", d3.forceManyBody().strength(1))
                        .alphaTarget(1).restart()
    },
    createViz () {

      // Prepares Tooltips
      var div = d3.select("body").append("div")
      .attr("class", "tooltip")
      .style("opacity", 0);

      function makeCard(d) {
        var title = d.title
        if (d.url != '') {
          title = `<a href="${d.url}" target="_blank">${d.title}</a>`
        }
        return `
          <div class="card">
            <header class="card-header">
              <p class="card-header-title">
                ${d.type}
              </p>
              <a class="card-header-icon" aria-label="close" onClick="var elems = document.getElementsByClassName('tooltip');for (var i = 0; i < elems.length; i++) {elems[i].style.opacity='0';elems[i].style['z-index']='-1'} ">
                <span class="icon">
                  <i class="fas fa-window-close" aria-hidden="true"></i>
                </span>
              </a>
            </header>
            <div class="card-content">
              <div class="content">
                ${title}, ${d.location}
              </div>
              <time>${moment(d.date).format("MMMM Do YYYY")}</time>
            </div>
          </div>
          `
      }

      this.simulation = d3.forceSimulation()
                        .nodes(this.nodes)
                        .force("charge_force", d3.forceManyBody().strength(1))
                        .force("center_force", d3.forceCenter(this.width / 2, this.height / 2))
                        .force('collision', d3.forceCollide(6))
                        .on("tick", tickActions );

      var node = this.svg.append("g")
              .attr("class", "nodes")
              .selectAll("circle")
              .data(this.nodes)
              .enter()
              .append("circle")
              .attr("r", 5)
              .attr("fill", eventColor)
              .call(d3.drag()
                .subject(dragsubject)
                .on("start",dragstarted)
                .on("drag",dragged)
                .on("end",dragended))
              .on("click", function(d) {
               div.transition()
                 .duration(100)
                 .style("opacity", 1)
                 .style("z-index", 10);
               div.html(makeCard(d))
                 .style("left", (d3.event.pageX) + "px")
                 .style("top", (d3.event.pageY - 28) + "px");
               })
              
      var self = this;
      function dragstarted(d)
       { 
          if (!d3.event.active) self.simulation.alphaTarget(0).restart();
          d3.event.subject.fx = d3.event.subject.x;
          d3.event.subject.fy = d3.event.subject.y;
       }

       function dragsubject() {
          return self.simulation.find(d3.event.x, d3.event.y);
        }

       function dragged() {
          d3.event.subject.fx = d3.event.x;
          d3.event.subject.fy = d3.event.y;
        }

        function dragended() {
          if (!d3.event.active) self.simulation.alphaTarget(0.3);
          d3.event.subject.fx = null;
          d3.event.subject.fy = null;
        }


      function eventColor(d) {
        if (d.type == "Training") {return "#a02073"}
        else if (d.type == "Interview") {return "#dbb64b"}
        else if (d.type == "Project") {return "#67c7d3"}
        else if (d.type == "Conference") {return "#2d616f"}
        else if (d.type == "Article") {return "#eb3721"}
      }

      function tickActions() {
        node
            .attr("cx", function(d) { return d.x; })
            .attr("cy", function(d) { return d.y; })
      }
    }
  }
}

</script>

<style lang="sass">

.card
  max-width: 300px

div.tooltip
  position: absolute

.year-label
  font-size: 0.8em
  fill: #999

.countries
  stroke: #fff
  stroke-linejoin: round
  fill: #eee
</style>
