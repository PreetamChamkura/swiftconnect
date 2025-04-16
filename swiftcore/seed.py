from swiftcore import create_app, db
from swiftcore.models import Song, Merch

app = create_app()

with app.app_context():
    db.session.add(Song(title="All Too Well", album="Red", era="Red"))
    db.session.add(Merch(name="Folklore Cardigan", image_url="url_here"))
    db.session.commit()