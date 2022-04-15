# Define run parameters that define an experiment
n_agents=(4 4)
n_actions=(5 5)
threshold=(1 1)
feature_histories=(1 1)

for str in ${n_agents[@]}; do
  echo $str
done

# How many times to run each experiment
n_runs=(1 2)

# Loop through experiments
for i in ${!n_runs[@]}; do
  echo "element $i is ${n_runs[$i]}"
  # Create folder for experiment (if it doesn't exit)
  experiment_folder="$n_agents""agents_""$n_actions""actions_""$threshold""threshold_"
  experiment_folder="$experiment_folder""$feature_histories""history"
  experiment_folder="$experiment_folder""TEST"
  echo $experiment_folder
  

  # Loop through individual runs

  # Create folders
  # Run
done

mkdir -p ./temp
mkdir -p ./$experiment_folder