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

var data1 = [1,2,3,5,67,87,6543,2,36,7];
var data2 = [1,2,3,5,67,87,6543,2,36,7];

var options = {
    series: [{
        name: 'Flies',
        data: data1
    }, {
        name: 'Spiders',
        data: data2
    }],
    chart: {
        id: 'chart2',
        type: 'line',
        height: 230,
        dropShadow: {
            enabled: true,
            enabledOnSeries: [1]
        },
        toolbar: {
            autoSelected: 'pan',
            show: false
        }
    },
    colors: ['#008FFB', '#00E396'],
    stroke: {
        width: [2, 6],
        curve: ['straight', 'monotoneCubic']
    },
    dataLabels: {
        enabled: false
    },
    fill: {
        opacity: [1, 0.75]
    },
    markers: {
        size: 0
    },
    yaxis: [{
        seriesName: 'Flies',
        axisTicks: {
            show: true,
            color: '#008FFB'
        },
        axisBorder: {
            show: true,
            color: '#008FFB'
        },
        labels: {
            style: {
                colors: '#008FFB'
            }
        },
        title: {
            text: "Flies",
            style: {
                color: '#008FFB'
            }
        }
    }, {
        seriesName: 'Spiders',
        opposite: true,
        axisTicks: {
            show: true,
            color: '#00E396'
        },
        axisBorder: {
            show: true,
            color: '#00E396'
        },
        labels: {
            style: {
                colors: '#00E396'
            }
        },
        title: {
            text: "Spiders",
            style: {
                color: '#00E396'
            }
        }
    }],
    xaxis: {
        type: 'datetime'
    }
};

var chart = new ApexCharts(document.querySelector("#chart-line2"), options);
chart.render();

var optionsLine = {
    series: [{
        name: 'Flies',
        data: data1
    }, {
        name: 'Spiders',
        data: data2
    }],
    chart: {
        id: 'chart1',
        height: 130,
        type: 'area',
        brush: {
            target: 'chart2',
            enabled: true
        },
        selection: {
            enabled: true,
            xaxis: {
                min: new Date('24 April 2017').getTime(),
                max: new Date('29 May 2017').getTime()
            }
        }
    },
    colors: ['#008FFB', '#00E396'],
    stroke: {
        width: [1, 3],
        curve: ['straight', 'monotoneCubic']
    },
    fill: {
        type: 'gradient',
        gradient: {
            opacityFrom: 0.91,
            opacityTo: 0.1
        }
    },
    xaxis: {
        type: 'datetime',
        tooltip: {
            enabled: false
        }
    },
    yaxis: {
        max: 100,
        tickAmount: 2
    }
};

var chartLine = new ApexCharts(document.querySelector("#chart-line"), optionsLine);
chartLine.render();

console.log('JavaScript is running');
