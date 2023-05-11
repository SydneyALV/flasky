from app import db

class Crystal(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    color = db.Column(db.String)
    powers = db.Column(db.String)
    healer_id = db.Column(db.Integer, db.ForeignKey('healer.id'))
    healer = db.relationship("Healer", back_populates="crystals")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "color": self.color,
            "powers": self.powers
        }

    @classmethod
    def from_dict(cls, crystal_data):
        new_crystal = cls(
            name = crystal_data["name"],
            color = crystal_data["color"],
            powers = crystal_data["powers"]
        )
        return new_crystal