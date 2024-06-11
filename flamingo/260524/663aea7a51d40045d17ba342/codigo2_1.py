import matplotlib.pyplot as plt


class Species:
    """Represents a chemical species with its initial concentration."""

    def __init__(self, name, concentration):
        if concentration < 0:
            raise ValueError("Initial concentration cannot be negative.")
        self.name = name
        self.concentration = concentration


class Reaction:
    """Represents a chemical reaction with reactants, products, and rate constants."""

    def __init__(self, reactants, products, rate_constant, reverse_rate_constant=None):
        if rate_constant < 0 or (
            reverse_rate_constant is not None and reverse_rate_constant < 0
        ):
            raise ValueError("Rate constants cannot be negative.")
        self.reactants = reactants
        self.products = products
        self.rate_constant = rate_constant
        self.reverse_rate_constant = reverse_rate_constant


class ReactionNetwork:
    """Simulates a chemical reaction network using the Euler method."""

    def __init__(
        self,
        species,
        reactions,
        equilibrium_threshold=1e-6,
        equilibrium_steps=10,
        plot_interval=1,
    ):
        self.species = {s.name: s for s in species}
        self.reactions = reactions
        self.equilibrium_threshold = equilibrium_threshold
        self.equilibrium_steps = equilibrium_steps
        self.plot_interval = plot_interval
        self.concentration_history = {s.name: [] for s in species}
        self.time_history = []

    def add_reaction(self, reaction):
        self.reactions.append(reaction)

    def simulate(self, time_step, total_time, output_interval):
        if time_step <= 0 or total_time <= 0 or output_interval <= 0:
            raise ValueError(
                "Time step, total time, and output interval must be positive."
            )

        species_concentrations = {
            s.name: s.concentration for s in self.species.values()
        }
        current_time = 0
        equilibrium_counter = 0
        previous_concentrations = {
            s.name: s.concentration for s in self.species.values()
        }

        while current_time <= total_time:
            # Output concentrations at specified intervals
            if current_time % output_interval == 0:
                print(f"Time: {current_time}")
                for species, concentration in species_concentrations.items():
                    print(f"{species}: {concentration}")
                print()

            # Update concentrations using the Euler method
            delta_concentrations = {}
            for reaction in self.reactions:
                reactant_concentrations = [
                    species_concentrations[reactant] for reactant in reaction.reactants
                ]
                product_concentrations = [
                    species_concentrations[product] for product in reaction.products
                ]

                # Calculate reaction rate
                forward_rate = reaction.rate_constant * eval(
                    "*".join(map(str, reactant_concentrations))
                )
                if reaction.reverse_rate_constant is not None:
                    reverse_rate = reaction.reverse_rate_constant * eval(
                        "*".join(map(str, product_concentrations))
                    )
                else:
                    reverse_rate = 0

                # Update delta concentrations
                for reactant in reaction.reactants:
                    delta_concentrations[reactant] = (
                        delta_concentrations.get(reactant, 0)
                        - forward_rate
                        + reverse_rate
                    )
                for product in reaction.products:
                    delta_concentrations[product] = (
                        delta_concentrations.get(product, 0)
                        + forward_rate
                        - reverse_rate
                    )

            # Update species concentrations
            for species, delta_concentration in delta_concentrations.items():
                species_concentrations[species] += delta_concentration * time_step

            # Update concentration history
            for species, concentration in species_concentrations.items():
                self.concentration_history[species].append(concentration)
            self.time_history.append(current_time)

            # Check for equilibrium
            concentration_changes = {
                species: abs(concentration - previous_concentrations[species])
                for species, concentration in species_concentrations.items()
            }
            if all(
                change < self.equilibrium_threshold
                for change in concentration_changes.values()
            ):
                equilibrium_counter += 1
                if equilibrium_counter >= self.equilibrium_steps:
                    print("Equilibrium reached at time:", current_time)
                    break
            else:
                equilibrium_counter = 0

            previous_concentrations = species_concentrations.copy()

            # Update plots
            if current_time % self.plot_interval == 0:
                for species in self.species:
                    plt.plot(
                        self.time_history,
                        self.concentration_history[species],
                        label=species,
                    )
                plt.xlabel("Time")
                plt.ylabel("Concentration")
                plt.legend()
                plt.show(block=False)
                plt.pause(0.01)
                plt.clf()

            current_time += time_step


# Example usage
species = [Species("A", 1.0), Species("B", 2.0), Species("C", 0.0)]

reactions = [
    Reaction(["A", "B"], ["C"], 0.1),
    Reaction(["C"], ["A", "B"], 0.05),  # Reversible reaction
]

network = ReactionNetwork(species, reactions)
network.simulate(0.01, 10, 1)

# Add a new reaction dynamically
new_reaction = Reaction(["A"], ["B"], 0.2)
network.add_reaction(new_reaction)
