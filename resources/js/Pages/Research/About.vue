<template>
    <MainLayout>
        <div class="bg-white py-16">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <SectionTitle 
                    title="About the Research"
                    subtitle="Understanding the background and significance of our project"
                />

                <!-- Research Background -->
                <section class="mb-16">
                    <div class="bg-gradient-to-r from-blue-gray to-blue-gray rounded-lg p-8 md:p-12 mb-8">
                        <h3 class="text-3xl font-bold text-gray-900 mb-6">Research Background</h3>
                        <p class="text-gray-700 text-lg leading-relaxed mb-4">
                            The global landscape of hiring is undergoing a transformation, shifting away from a system that prioritizes educational credentials toward one that values demonstrable competency. This "skills-first" paradigm prioritizes knowledge and abilities over formal degrees, designed to expand talent pools and improve how people are matched to jobs.
                        </p>
                        <p class="text-gray-700 text-lg leading-relaxed mb-4">
                            Despite these shifts, the hiring process is still filled with conflicts. Employers struggle to identify the right talent, often relying on ambiguous and overstuffed job postings that fail to articulate precise requirements. Qualified candidates often get discouraged and preemptively exclude themselves from the application process. This issue is particularly acute in developing economies like the Philippines, which has a documented history of labor mismatch where workers are frequently over-skilled or under-skilled, lacking the requisite competencies for their current roles.
                        </p>
                        <p class="text-gray-700 text-lg leading-relaxed">
                            Statistical data confirms the severity of this structural gap. Approximately 35% of workers in OECD countries are mismatched by qualification. In the Philippines, studies regarding Technical Vocational and Livelihood (TVL) graduates in Butuan City revealed a mismatch incidence of 64%, indicating a severe failure to align educational specialization with employment outcomes. Furthermore, national data indicates that youth unemployment rates have reached 13.5%, more than double the national average.
                        </p>
                    </div>
                </section>

                <!-- Importance Section -->
                <section class="mb-16">
                    <h3 class="text-3xl font-bold text-gray-900 mb-6">Why This Research Matters</h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div class="border-l-4 border-customButton pl-6 py-4">
                            <h4 class="text-xl font-semibold text-gray-900 mb-2">Addresses Skills Mismatch</h4>
                            <p class="text-gray-600">
                                When the workforce disconnects from market needs, vulnerable populations suffer the most, facing career trajectories defined by lower lifetime earnings and reduced job satisfaction. On a macroeconomic scale, this skills mismatch serves as a primary driver of productivity loss.
                            </p>
                        </div>
                        <div class="border-l-4 border-customblue pl-6 py-4">
                            <h4 class="text-xl font-semibold text-gray-900 mb-2">Zero-Cost Access</h4>
                            <p class="text-gray-600">
                                While digital platforms function as primary intermediaries in the labor market, accessing high-quality training necessary to bridge skill gaps is often financially prohibitive. Pathfinder provides a direct economic intervention by curating zero-cost resources, thereby promoting equity.
                            </p>
                        </div>
                        <div class="border-l-4 border-customdarkblue pl-6 py-4">
                            <h4 class="text-xl font-semibold text-gray-900 mb-2">Skills-Based Hiring Benefits</h4>
                            <p class="text-gray-600">
                                Research indicates that non-degreed workers hired into roles based on skills demonstrate a 10-percentage point higher retention rate and realize a 25% salary increase compared to their previous roles. Enabling a genuine skills-based hiring approach is mutually beneficial.
                            </p>
                        </div>
                        <div class="border-l-4 border-customButton pl-6 py-4">
                            <h4 class="text-xl font-semibold text-gray-900 mb-2">Centralized Platform</h4>
                            <p class="text-gray-600">
                                The study addresses the need for a centralized platform to access different organizations' training programs that increase job prospects in a competitive job market. By combining various training programs and career opportunities into a user-friendly web application, Pathfinder empowers college students and job seekers.
                            </p>
                        </div>
                    </div>
                </section>

                <!-- Problem Statement -->
                <section class="bg-red-50 border-l-4 border-red-500 rounded-lg p-8 md:p-12">
                    <h3 class="text-3xl font-bold text-gray-900 mb-6">Problem Statement</h3>
                    <p class="text-gray-700 text-lg leading-relaxed mb-4">
                        Existing workforce technologies, such as machine learning-based career guidance systems, have demonstrated viability in offering tailored career suggestions. However, a critical research gap remains regarding the convergence of functional specificity and economic accessibility. Current platforms often fail to provide a standardized, automated linkage between employer skill demands and cost-free skill acquisition pathways.
                    </p>
                    <p class="text-gray-700 text-lg leading-relaxed mb-4">
                        There is a distinct need for systems that enhance "skill signaling," explicitly linking required KSAs (Knowledge, Skills, and Abilities) to recognized credentials, to assist candidates in understanding which skills yield labor market value. Furthermore, many firms that claim to remove degree requirements fail to alter their actual hiring behavior, often because they lack the internal processes to validate skills without educational proxies.
                    </p>
                    <p class="text-gray-700 text-lg leading-relaxed">
                        While social media platforms and job portals exist, they lack integration with training or skill development resources that are crucial for enhancing an applicant's employability. These systems provide minimal to no support to users when it comes to skill development because they focus heavily on matching applicants with employers. This highlights the need for a unified platform that not only connects users with job opportunities but also empowers them to upskill and prepare through accessible training programs.
                    </p>
                </section>
            </div>
        </div>
    </MainLayout>
</template>

<script setup>
import MainLayout from '@/Layouts/MainLayout.vue';
import SectionTitle from '@/Components/SectionTitle.vue';
</script>

