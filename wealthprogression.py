st.write(f"""
 ## Experiment Parameters
 * Initial Wealth = ${sl_initial _wealth}
 * Faster Growth Percentage = {sl_fast_growth_pct)%    
 * Slower Growth Percentage ={sl_slow_growth_pct)%
 * Time Steps = 60
 * Number of Individuals = 1000
 * Probability of Faster Growth = {sl_probability_faster_growth}
  """)

 if st.sidebar.button("Run Experiment"):
         run_experiment(sl_initial_wealth,sl_fast_growth_pct,sl_slow_growth_pct)
         
