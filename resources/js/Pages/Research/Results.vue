<template>
    <MainLayout>
        <div class="bg-white py-16">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <SectionTitle 
                    title="Research Results"
                    subtitle="Findings, insights, and outcomes of our research"
                />

                <!-- Key Findings -->
                <section class="mb-16">
                    <h3 class="text-3xl font-bold text-gray-900 mb-8">Key Findings</h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div 
                            v-for="(finding, index) in findings" 
                            :key="index"
                            class="bg-gradient-to-br from-indigo-50 to-purple-50 rounded-lg p-6 border-l-4 border-indigo-600"
                        >
                            <div class="flex items-center mb-3">
                                <div class="w-10 h-10 bg-indigo-600 text-white rounded-full flex items-center justify-center font-bold mr-3">
                                    {{ index + 1 }}
                                </div>
                                <h4 class="text-xl font-semibold text-gray-900">{{ finding.title }}</h4>
                            </div>
                            <p class="text-gray-700">{{ finding.description }}</p>
                        </div>
                    </div>
                </section>

                <!-- Results Summary -->
                <section class="mb-16">
                    <div class="bg-green-50 border-l-4 border-green-500 rounded-lg p-8 md:p-12">
                        <h3 class="text-3xl font-bold text-gray-900 mb-6">Results Summary</h3>
                        <p class="text-gray-700 text-lg leading-relaxed mb-4">
                            The Pathfinder web application was successfully constructed using the Rapid Application Development (RAD) model, achieving stable and reliable deployment from local development to live production environment on Render. The project successfully implemented all intended software modules designed to bridge the gap between skill acquisition and employment.
                        </p>
                        <p class="text-gray-700 text-lg leading-relaxed mb-4">
                            Key features including the Career-Training Matching Engine, Resume Editor, and QR code-based attendance and certificate issuance system effectively digitized processes that were previously done manually. The system was validated against ISO/IEC 25010 and USE model standards, confirming that Pathfinder is a significant improvement over existing disjointed platforms.
                        </p>
                        <p class="text-gray-700 text-lg leading-relaxed">
                            Ultimately, this project addresses the critical economic challenge of skills mismatch in the localized labor market of Tuguegarao City. By providing a zero-cost, centralized platform that links skills-first training opportunities directly to career paths, Pathfinder empowers vulnerable populations—specifically unemployed youth and low-income job seekers—to enhance their employability without financial barriers.
                        </p>
                    </div>
                </section>

                <!-- Insights -->
                <section class="mb-16">
                    <h3 class="text-3xl font-bold text-gray-900 mb-8">Key Insights</h3>
                    <div class="space-y-6">
                        <div 
                            v-for="(insight, index) in insights" 
                            :key="index"
                            class="flex items-start bg-white border-2 border-gray-200 rounded-lg p-6 hover:border-indigo-500 hover:shadow-lg transition-all duration-300"
                        >
                            <div class="flex-shrink-0 w-12 h-12 bg-purple-100 rounded-lg flex items-center justify-center mr-4">
                                <span class="text-purple-600 text-xl">💡</span>
                            </div>
                            <div class="flex-1">
                                <h4 class="text-lg font-semibold text-gray-900 mb-2">{{ insight.title }}</h4>
                                <p class="text-gray-600">{{ insight.description }}</p>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- Research Metrics with Charts -->
                <section class="bg-gray-50 rounded-lg p-8 md:p-12 mb-16">
                    <h3 class="text-3xl font-bold text-gray-900 mb-8 text-center">Research Metrics</h3>
                    
                    <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-8">
                        <!-- Overall Ratings Chart -->
                        <div class="bg-white rounded-lg p-6 shadow-md">
                            <h4 class="text-xl font-semibold text-gray-900 mb-4">Overall Ratings Comparison</h4>
                            <div class="h-64 flex items-center justify-center">
                                <canvas ref="overallRatingsChart" width="400" height="256"></canvas>
                            </div>
                        </div>

                        <!-- Evaluators Count Chart -->
                        <div class="bg-white rounded-lg p-6 shadow-md">
                            <h4 class="text-xl font-semibold text-gray-900 mb-4">Evaluator Participation</h4>
                            <div class="h-64 flex items-center justify-center">
                                <canvas ref="evaluatorsChart" width="400" height="256"></canvas>
                            </div>
                        </div>
                    </div>

                    <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
                        <!-- USE Questionnaire Scores -->
                        <div class="bg-white rounded-lg p-6 shadow-md">
                            <h4 class="text-xl font-semibold text-gray-900 mb-4">USE Questionnaire Scores</h4>
                            <div class="h-64 flex items-center justify-center">
                                <canvas ref="useQuestionnaireChart" width="400" height="256"></canvas>
                            </div>
                        </div>

                        <!-- ISO/IEC 25010 Characteristics -->
                        <div class="bg-white rounded-lg p-6 shadow-md">
                            <h4 class="text-xl font-semibold text-gray-900 mb-4">ISO/IEC 25010 Quality Characteristics</h4>
                            <div class="h-64 flex items-center justify-center">
                                <canvas ref="isoCharacteristicsChart" width="400" height="256"></canvas>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- Data Visualizations -->
                <section class="mb-16">
                    <h3 class="text-3xl font-bold text-gray-900 mb-8 text-center">Data Visualizations</h3>
                    
                    <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-12">
                        <!-- Pie Chart: End User Evaluators Distribution -->
                        <div class="bg-white rounded-lg p-6 shadow-lg border-2 border-gray-200">
                            <h4 class="text-xl font-bold text-gray-900 mb-4 text-center">End User Evaluators Distribution</h4>
                            <div class="h-80 flex items-center justify-center">
                                <canvas ref="endUserPieChart" width="400" height="400"></canvas>
                            </div>
                        </div>

                        <!-- Bar Chart: IT Experts Specialization -->
                        <div class="bg-white rounded-lg p-6 shadow-lg border-2 border-gray-200">
                            <h4 class="text-xl font-bold text-gray-900 mb-4 text-center">IT Experts Specialization</h4>
                            <div class="h-80 flex items-center justify-center">
                                <canvas ref="itExpertsBarChart" width="400" height="400"></canvas>
                            </div>
                        </div>
                    </div>

                    <!-- USE Mean Ratings -->
                    <div class="bg-white rounded-lg p-8 shadow-lg border-2 border-gray-200 mb-8">
                        <h4 class="text-2xl font-bold text-gray-900 mb-6 text-center">USE Questionnaire Mean Ratings</h4>
                        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                            <div 
                                v-for="(useItem, index) in useRatings" 
                                :key="index"
                                class="text-center"
                            >
                                <p class="text-gray-700 font-semibold mb-3">{{ useItem.characteristic }}</p>
                                <div class="flex justify-center items-center gap-1 mb-2">
                                    <svg 
                                        v-for="star in 5" 
                                        :key="star"
                                        class="w-6 h-6"
                                        :class="star <= useItem.stars ? 'text-yellow-400' : 'text-gray-300'"
                                        fill="currentColor" 
                                        viewBox="0 0 20 20"
                                    >
                                        <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                                    </svg>
                                </div>
                                <p class="text-lg font-bold text-indigo-600">{{ useItem.mean }}</p>
                                <p class="text-sm text-gray-500">{{ useItem.label }}</p>
                            </div>
                        </div>
                    </div>

                    <!-- ISO Mean Ratings -->
                    <div class="bg-white rounded-lg p-8 shadow-lg border-2 border-gray-200">
                        <h4 class="text-2xl font-bold text-gray-900 mb-6 text-center">ISO/IEC 25010 Mean Ratings</h4>
                        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-6">
                            <div 
                                v-for="(isoItem, index) in isoRatings" 
                                :key="index"
                                class="text-center"
                            >
                                <p class="text-gray-700 font-semibold mb-3">{{ isoItem.characteristic }}</p>
                                <div class="flex justify-center items-center gap-1 mb-2">
                                    <svg 
                                        v-for="star in 5" 
                                        :key="star"
                                        class="w-6 h-6"
                                        :class="star <= isoItem.stars ? 'text-yellow-400' : 'text-gray-300'"
                                        fill="currentColor" 
                                        viewBox="0 0 20 20"
                                    >
                                        <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                                    </svg>
                                </div>
                                <p class="text-lg font-bold text-indigo-600">{{ isoItem.mean }}</p>
                                <p class="text-sm text-gray-500">{{ isoItem.label }}</p>
                            </div>
                        </div>
                    </div>
                </section>
            </div>
        </div>
    </MainLayout>
</template>

<script setup>
import { ref, onMounted, nextTick } from 'vue';
import { Chart, registerables } from 'chart.js';
import MainLayout from '@/Layouts/MainLayout.vue';
import SectionTitle from '@/Components/SectionTitle.vue';

Chart.register(...registerables);

const findings = ref([
    {
        title: 'High End-User Satisfaction',
        description: 'The web application achieved an overall mean rating of 4.55 (Strongly Agree) from 34 end-users, with "Ease of Use" receiving the highest individual score of 4.64. This indicates that the interface design was highly intuitive for college students and job seekers.'
    },
    {
        title: 'Strong Technical Quality',
        description: 'Evaluation by 13 IT experts yielded an overall mean of 4.07 (Agree) based on ISO/IEC 25010 standards, with "Portability" scoring highest at 4.15, confirming the system\'s adaptability across different operational environments.'
    },
    {
        title: 'Excellent Usability Metrics',
        description: 'All USE Questionnaire criteria received "Strongly Agree" ratings: Usefulness (4.63), Ease of Use (4.64), Ease of Learning (4.51), and Satisfaction (4.43). Users could quickly master the web application functionalities without extensive instruction.'
    },
    {
        title: 'Comprehensive Quality Standards',
        description: 'All ISO/IEC 25010 characteristics received "Agree" ratings: Functional Suitability (4.03), Compatibility (4.08), Usability (4.08), Security (4.00), and Portability (4.15), confirming the system successfully met its objectives.'
    }
]);

const insights = ref([
    {
        title: 'User-Centric Design Success',
        description: 'The high "Ease of Use" rating (4.64) demonstrates that the interface design, specifically the navigation flows for searching careers and trainings, was intuitive for the target audience. This validates the effectiveness of the RAD methodology\'s emphasis on continuous user involvement and iterative refinement.'
    },
    {
        title: 'Centralized Platform Value',
        description: 'The "Usefulness" rating of 4.63 confirms that respondents found the web application\'s core purpose of centralizing training and career opportunities highly relevant to their needs. This addresses the critical gap in existing platforms that require users to navigate multiple websites.'
    },
    {
        title: 'Technical Adaptability',
        description: 'The highest-rated ISO 25010 characteristic was "Portability" (4.15), indicating that experts found the web application adaptable across different environments and devices. This confirms the system\'s readiness for broader deployment beyond Tuguegarao City.'
    },
    {
        title: 'Skills-Based Approach Validation',
        description: 'The positive evaluation results validate Pathfinder\'s approach to skills-based hiring. The system successfully provides a centralized, secure, and compatible platform that effectively replaces the need to navigate multiple websites for training and job applications, addressing the skills mismatch challenge.'
    }
]);

const metrics = ref([
    { value: '4.55', label: 'Overall End-User Rating (Strongly Agree)' },
    { value: '4.64', label: 'Ease of Use Score (Highest)' },
    { value: '34', label: 'End-User Evaluators' },
    { value: '13', label: 'IT Expert Evaluators' },
    { value: '4.07', label: 'Overall Expert Rating (Agree)' },
    { value: '4.15', label: 'Portability Score (Highest)' }
]);

// Chart refs
const endUserPieChart = ref(null);
const itExpertsBarChart = ref(null);
const overallRatingsChart = ref(null);
const evaluatorsChart = ref(null);
const useQuestionnaireChart = ref(null);
const isoCharacteristicsChart = ref(null);

// USE Ratings Data
const useRatings = ref([
    { characteristic: 'Usefulness', mean: '4.63', stars: 5, label: 'Strongly Agree' },
    { characteristic: 'Ease of Use', mean: '4.64', stars: 5, label: 'Strongly Agree' },
    { characteristic: 'Ease of Learning', mean: '4.51', stars: 5, label: 'Strongly Agree' },
    { characteristic: 'Satisfaction', mean: '4.43', stars: 4, label: 'Strongly Agree' }
]);

// ISO Ratings Data
const isoRatings = ref([
    { characteristic: 'Functional Suitability', mean: '4.03', stars: 4, label: 'Agree' },
    { characteristic: 'Compatibility', mean: '4.08', stars: 4, label: 'Agree' },
    { characteristic: 'Usability', mean: '4.08', stars: 4, label: 'Agree' },
    { characteristic: 'Security', mean: '4.00', stars: 4, label: 'Agree' },
    { characteristic: 'Portability', mean: '4.15', stars: 4, label: 'Agree' }
]);

// End User Evaluators Distribution Data (example - adjust based on actual data)
const endUserDistribution = {
    labels: ['College Students', 'Job Seekers', 'Other'],
    data: [20, 12, 2], // Total: 34
    backgroundColor: [
        'rgba(99, 102, 241, 0.8)', // indigo
        'rgba(139, 92, 246, 0.8)', // purple
        'rgba(168, 85, 247, 0.8)'  // violet
    ],
    borderColor: [
        'rgba(99, 102, 241, 1)',
        'rgba(139, 92, 246, 1)',
        'rgba(168, 85, 247, 1)'
    ]
};

// IT Experts Specialization Data (example - adjust based on actual data)
const itExpertsSpecialization = {
    labels: ['Software Development', 'System Architecture', 'Quality Assurance', 'Database Management', 'Security'],
    data: [4, 3, 2, 2, 2], // Total: 13
    backgroundColor: 'rgba(99, 102, 241, 0.8)',
    borderColor: 'rgba(99, 102, 241, 1)',
    borderWidth: 1
};

onMounted(async () => {
    await nextTick();
    
    try {
        // Create Pie Chart for End User Evaluators
        if (endUserPieChart.value) {
            new Chart(endUserPieChart.value, {
                type: 'pie',
                data: {
                    labels: endUserDistribution.labels,
                    datasets: [{
                        data: endUserDistribution.data,
                        backgroundColor: endUserDistribution.backgroundColor,
                        borderColor: endUserDistribution.borderColor,
                        borderWidth: 2
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            position: 'bottom',
                            labels: {
                                padding: 15,
                                font: {
                                    size: 12
                                }
                            }
                        },
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    const label = context.label || '';
                                    const value = context.parsed || 0;
                                    const total = context.dataset.data.reduce((a, b) => a + b, 0);
                                    const percentage = ((value / total) * 100).toFixed(1);
                                    return `${label}: ${value} (${percentage}%)`;
                                }
                            }
                        }
                    }
                }
            });
        } else {
            console.error('Pie chart canvas element not found');
        }

        // Create Bar Chart for IT Experts Specialization
        if (itExpertsBarChart.value) {
            new Chart(itExpertsBarChart.value, {
                type: 'bar',
                data: {
                    labels: itExpertsSpecialization.labels,
                    datasets: [{
                        label: 'Number of Experts',
                        data: itExpertsSpecialization.data,
                        backgroundColor: itExpertsSpecialization.backgroundColor,
                        borderColor: itExpertsSpecialization.borderColor,
                        borderWidth: itExpertsSpecialization.borderWidth
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        y: {
                            beginAtZero: true,
                            ticks: {
                                stepSize: 1,
                                font: {
                                    size: 11
                                }
                            },
                            grid: {
                                color: 'rgba(0, 0, 0, 0.05)'
                            }
                        },
                        x: {
                            ticks: {
                                font: {
                                    size: 10
                                },
                                maxRotation: 45,
                                minRotation: 45
                            },
                            grid: {
                                display: false
                            }
                        }
                    },
                    plugins: {
                        legend: {
                            display: false
                        },
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    return `Experts: ${context.parsed.y}`;
                                }
                            }
                        }
                    }
                }
            });
        } else {
            console.error('Bar chart canvas element not found');
        }

        // Wait a bit more for DOM to be fully ready
        await new Promise(resolve => setTimeout(resolve, 100));

        // Create Overall Ratings Comparison Chart
        if (overallRatingsChart.value) {
            console.log('Creating Overall Ratings Chart');
            new Chart(overallRatingsChart.value, {
                type: 'bar',
                data: {
                    labels: ['End-User Rating', 'Expert Rating', 'Ease of Use', 'Portability'],
                    datasets: [{
                        label: 'Rating Score',
                        data: [4.55, 4.07, 4.64, 4.15],
                        backgroundColor: [
                            'rgba(99, 102, 241, 0.8)',
                            'rgba(139, 92, 246, 0.8)',
                            'rgba(59, 130, 246, 0.8)',
                            'rgba(168, 85, 247, 0.8)'
                        ],
                        borderColor: [
                            'rgba(99, 102, 241, 1)',
                            'rgba(139, 92, 246, 1)',
                            'rgba(59, 130, 246, 1)',
                            'rgba(168, 85, 247, 1)'
                        ],
                        borderWidth: 2
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            display: false
                        },
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    return `Score: ${context.parsed.y.toFixed(2)}`;
                                }
                            }
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            max: 5,
                            ticks: {
                                stepSize: 0.5
                            },
                            grid: {
                                color: 'rgba(0, 0, 0, 0.05)'
                            }
                        },
                        x: {
                            grid: {
                                display: false
                            }
                        }
                    }
                }
            });
        }

        // Create Evaluators Participation Chart
        if (evaluatorsChart.value) {
            console.log('Creating Evaluators Chart');
            new Chart(evaluatorsChart.value, {
                type: 'doughnut',
                data: {
                    labels: ['End-User Evaluators', 'IT Expert Evaluators'],
                    datasets: [{
                        data: [34, 13],
                        backgroundColor: [
                            'rgba(99, 102, 241, 0.8)',
                            'rgba(139, 92, 246, 0.8)'
                        ],
                        borderColor: [
                            'rgba(99, 102, 241, 1)',
                            'rgba(139, 92, 246, 1)'
                        ],
                        borderWidth: 2
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            position: 'bottom',
                            labels: {
                                padding: 15
                            }
                        },
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    const label = context.label || '';
                                    const value = context.parsed || 0;
                                    const total = context.dataset.data.reduce((a, b) => a + b, 0);
                                    const percentage = ((value / total) * 100).toFixed(1);
                                    return `${label}: ${value} (${percentage}%)`;
                                }
                            }
                        }
                    }
                }
            });
        }

        // Create USE Questionnaire Scores Chart
        if (useQuestionnaireChart.value) {
            console.log('Creating USE Questionnaire Chart');
            new Chart(useQuestionnaireChart.value, {
                type: 'bar',
                data: {
                    labels: ['Usefulness', 'Ease of Use', 'Ease of Learning', 'Satisfaction'],
                    datasets: [{
                        label: 'Score',
                        data: [4.63, 4.64, 4.51, 4.43],
                        backgroundColor: [
                            'rgba(99, 102, 241, 0.8)',
                            'rgba(139, 92, 246, 0.8)',
                            'rgba(59, 130, 246, 0.8)',
                            'rgba(168, 85, 247, 0.8)'
                        ],
                        borderColor: [
                            'rgba(99, 102, 241, 1)',
                            'rgba(139, 92, 246, 1)',
                            'rgba(59, 130, 246, 1)',
                            'rgba(168, 85, 247, 1)'
                        ],
                        borderWidth: 2
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            display: false
                        },
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    return `Score: ${context.parsed.y.toFixed(2)}`;
                                }
                            }
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            max: 5,
                            ticks: {
                                stepSize: 0.5
                            },
                            grid: {
                                color: 'rgba(0, 0, 0, 0.05)'
                            }
                        },
                        x: {
                            grid: {
                                display: false
                            }
                        }
                    }
                }
            });
        }

        // Create ISO/IEC 25010 Characteristics Chart
        if (isoCharacteristicsChart.value) {
            console.log('Creating ISO Characteristics Chart');
            new Chart(isoCharacteristicsChart.value, {
                type: 'bar',
                data: {
                    labels: ['Functional Suitability', 'Compatibility', 'Usability', 'Security', 'Portability'],
                    datasets: [{
                        label: 'Rating Score',
                        data: [4.03, 4.08, 4.08, 4.00, 4.15],
                        backgroundColor: [
                            'rgba(99, 102, 241, 0.8)',
                            'rgba(139, 92, 246, 0.8)',
                            'rgba(59, 130, 246, 0.8)',
                            'rgba(168, 85, 247, 0.8)',
                            'rgba(124, 58, 237, 0.8)'
                        ],
                        borderColor: [
                            'rgba(99, 102, 241, 1)',
                            'rgba(139, 92, 246, 1)',
                            'rgba(59, 130, 246, 1)',
                            'rgba(168, 85, 247, 1)',
                            'rgba(124, 58, 237, 1)'
                        ],
                        borderWidth: 2
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            display: false
                        },
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    return `Score: ${context.parsed.y.toFixed(2)}`;
                                }
                            }
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            max: 5,
                            ticks: {
                                stepSize: 0.5
                            },
                            grid: {
                                color: 'rgba(0, 0, 0, 0.05)'
                            }
                        },
                        x: {
                            ticks: {
                                font: {
                                    size: 10
                                },
                                maxRotation: 45,
                                minRotation: 45
                            },
                            grid: {
                                display: false
                            }
                        }
                    }
                }
            });
        }
    } catch (error) {
        console.error('Error creating charts:', error);
    }
});
</script>

