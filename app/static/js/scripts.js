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
}
};

var chart = new ApexCharts(document.querySelector("#chart"), options);
chart.render();
