PYTHON_ADD_MODULE(quantumMC SchroedingerDiffusionMC.cxx PathIntegralMC.cxx quantumMCPython.cxx)
target_link_libraries(quantumMC ${Boost_LIBRARIES} boost_python)

