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

    def __init__(self, species, reactions):
        self.species = {s.name: s for s in species}
        self.reactions = reactions

    def simulate(self, time_step, total_time, output_interval):
        if time_step <= 0 or total_time <= 0 or output_interval <= 0:
            raise ValueError(
                "Time step, total time, and output interval must be positive."
            )

        species_concentrations = {
            s.name: s.concentration for s in self.species.values()
        }
        current_time = 0

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

            current_time += time_step


# Example usage
species = [Species("A", 6.0), Species("B", 2.0), Species("C", 1.0)]

reactions = [
    Reaction(["A", "B", "C"], ["A", "C"], 0.00001),
    Reaction(["C"], ["A", "B"], 0.0005),  # Reversible reaction
]

network = ReactionNetwork(species, reactions)
network.simulate(1, 100, 0.1)
