# Define a class to represent a chemical species
class Species:
    def __init__(self, name, initial_concentration):
        self.name = name
        self.initial_concentration = initial_concentration
        self.concentration = initial_concentration


# Define a class to represent a reaction
class Reaction:
    def __init__(
        self,
        reactants,
        products,
        rate_constant,
        reversible=False,
        reverse_rate_constant=None,
    ):
        self.reactants = reactants
        self.products = products
        self.rate_constant = rate_constant
        self.reversible = reversible
        self.reverse_rate_constant = reverse_rate_constant


# Define a function to validate input data
def validate_input(species, reactions):
    # Check for negative concentrations or rate constants
    for s in species:
        if s.initial_concentration < 0:
            raise ValueError(f"Negative initial concentration for species {s.name}")
    for r in reactions:
        if r.rate_constant < 0:
            raise ValueError(
                f"Negative rate constant for reaction {r.reactants} -> {r.products}"
            )
        if r.reversible and r.reverse_rate_constant < 0:
            raise ValueError(
                f"Negative reverse rate constant for reaction {r.reactants} -> {r.products}"
            )


# Define a function to simulate the chemical reaction network
def simulate(species, reactions, time_step, total_time, output_interval):
    # Initialize time and concentrations
    time = 0
    concentrations = {s.name: s.initial_concentration for s in species}

    # Simulate the reaction network using the Euler method
    while time <= total_time:
        # Calculate the reaction rates
        reaction_rates = {}
        for r in reactions:
            reactant_concentrations = [concentrations[s] for s in r.reactants]
            product_concentrations = [concentrations[s] for s in r.products]
            reaction_rate = r.rate_constant * np.prod(reactant_concentrations)
            if r.reversible:
                reaction_rate -= r.reverse_rate_constant * np.prod(
                    product_concentrations
                )
            reaction_rates[r] = reaction_rate

        # Update the concentrations using the Euler method
        for s in species:
            concentration_change = 0
            for r in reactions:
                if s.name in r.reactants:
                    concentration_change -= reaction_rates[r]
                if s.name in r.products:
                    concentration_change += reaction_rates[r]
            concentrations[s.name] += concentration_change * time_step

        # Output the concentrations at the specified interval
        if time % output_interval == 0:
            print(f"Time: {time:.2f}")
            for s in species:
                print(f"{s.name}: {concentrations[s.name]:.2f}")

        # Increment time
        time += time_step


# Example usage
species = [Species("A", 1.0), Species("B", 2.0), Species("C", 3.0)]

reactions = [
    Reaction(["A", "B"], ["C"], 0.1),
    Reaction(["C"], ["A", "B"], 0.2, reversible=True, reverse_rate_constant=0.3),
]

validate_input(species, reactions)
simulate(species, reactions, time_step=0.01, total_time=10.0, output_interval=1.0)
