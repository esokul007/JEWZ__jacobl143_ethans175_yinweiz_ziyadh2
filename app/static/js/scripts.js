function toggleHidden(id) {
    const toggle = document.getElementById(id);
    toggle.classList.toggle('hidden');
}

function jump(h) {
    const target = document.getElementById(h);
    if (target) {
        target.scrollIntoView({ behavior: 'smooth' });
    } else {
        console.warn(`Element with ID "${h}" not found.`);
    }
}

var options = {
  series: [{
    name: "Daily Stock Data",
    data: data2
}],
chart: {
  height: 350,
  type: 'line',
  zoom: {
    enabled: true,
    type: 'x', // Enable zooming on the x-axis only
    autoScaleYaxis: true, // Adjust y-axis automatically when zooming
  },
  toolbar: {
    tools: {
      zoom: true,
      zoomin: true,
      zoomout: true,
      pan: true,
      reset: true, // Add a reset zoom button
    },
  },
},
dataLabels: {
  enabled: false
},
stroke: {
  curve: 'straight'
},
title: {
  text: stockName,
  align: 'left'
},
grid: {
  row: {
    colors: ['#f3f3f3', 'transparent'],
    opacity: 0.5
  },
},
xaxis: {
  categories: data1,
  tickAmount: 20,
},
annotations: {
  xaxis: [
      {
          // x: "2015-01-29", // Must match one of the entries in data1
          // borderColor: '#00E396',
          // label: {
          //     borderColor: '#00E396',
          //     style: {
          //         color: '#fff',
          //         background: '#00E396'
          //     },
          //     text: 'Stock Spike'
          // } Test
      }
  ]
}

};

// var chart = new ApexCharts(document.querySelector("#chart"), options);
// chart.render();

// // Update Title
// document.getElementById("update-title").addEventListener("click", function() {
// const newTitle = document.getElementById("chart-title").value;
// if (newTitle) {
//   chart.updateOptions({
//       title: {
//           text: newTitle
//       }
//   });
//   console.log("I ran!")
// }
// });

// // Update Data
// document.getElementById("update-data").addEventListener("click", function() {
// const newData = document.getElementById("new-data").value;
// try {
//   const newDataArray = JSON.parse(newData);
//   chart.updateSeries([{
//       name: "Updated Data",
//       data: newDataArray
//   }]);
// } catch (e) {
//   console.error("Invalid data format. Enter data as an array, e.g., [10, 20, 30].");
// }
// });

// Add Annotation
document.addEventListener("DOMContentLoaded", function () {
  var chart = new ApexCharts(document.querySelector("#chart"), options);
  chart.render();

  document.getElementById("add-annotation").addEventListener("click", function () {
    const annotationText = document.getElementById("annotation").value;
    const annotationX = document.getElementById("annotation-x").value;

    console.log("Button clicked!");

    if (annotationText && annotationX) {
        chart.addXaxisAnnotation({
            x: annotationX, // must match an entry in data1
            borderColor: '#FF4560',
            label: {
                text: annotationText,
                style: {
                    background: "#FF4560",
                    color: "#fff"
                }
            }
        });
        console.log("Annotation added for:", annotationX);
    }
  });
});
