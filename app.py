from flask import Flask, render_template
app = Flask(__name__)

frettir=[
	[0,
	"Fjöldi lát­inna muni aldrei kom­ast á hreint",
	"Tala lát­inna er ekki kom­in á hreint en ég veit samt að lík­húsið er yf­ir­fullt. Regl­urn­ar hérna eru þær að ef þú ert ekki fund­inn þá ertu ekki úr­sk­urðaður lát­inn og ef það er ekki búið að bera kennsl á ákveðið lík þá er viðkom­andi ekki úr­sk­urðaður lát­inn held­ur,“ seg­ir Völ­und­ur Snær Völ­und­ar­son mat­reiðslumaður í sam­tali við mbl.is.",
	"Völ­und­ur er stadd­ur á Grand Bahama-eyju á Bahama­eyj­um þar sem hann hjálp­ar bág­stödd­um fórn­ar­lömb­um fimmta stigs felli­byls­ins Dori­an sem skreið yfir Bahama­eyj­ar í byrj­un mánaðar með skelfi­leg­um af­leiðing­um. Fjöl­marg­ir létu lífið, enn fleiri misstu heim­ili sín og þær bygg­ing­ar sem stóðu byl­inn af sér eru raf­magns­laus­ar og án renn­andi vatns.",
	"kristinn@mbl.is"],
	[1,
	"Liggur í dái eftir að hafa notað andlitskrem",
	"47 ára gömul kona staulaðist á bráðamóttöku í Sacramento í Kaliforníu fyrr í sumar.",
	"Konan var þoglumælt og kvartaði undan dofa í andliti og höndum. Skömmu síðar leið yfir hana og hún féll í dá en hún hefur legið í dái vikum saman núna. Stjórnendur í heilbrigðisgeiranum hafa nú fundið það sem olli því að konan fór í þetta ástand en það var andlitskrem sem hún keypti í Mexíkó.",
	"Nonni@bleikt.is"],
	[2,
	"Mike Pence til Íslands",
	"Mögu­legt er að Mike Pence, vara­for­seti Banda­ríkj­anna, sé á leið til lands­ins á næstu vik­um. Mun hann þá funda með Guðlaugi Þór Þórðar­syni ut­an­rík­is­ráðherra um viðskipta­sam­ráð Íslands og Banda­ríkj­anna. ",
	"MikePence@LateNews.com"],
	[3,
	"Þegar Atli Eðvalds­son hundskammaði Eið Smára",
	"Eiður Smári Guðjohnsen og Sverr­ir Þór Sverris­son (Sveppi) hittu Atla Eðvalds­son, fyrr­ver­andi landsliðsfyr­irliða og landsliðsþjálf­ara í knatt­spyrnu, við gerð Guðjohnsen-þátt­anna, þátta um fer­il Eiðs Smára sem Sveppi vann að og birt­ir voru í Sjón­varpi Sím­ans. Atli lést sem kunn­ugt er 2. sept­em­ber og var út­för hans gerð frá Hall­gríms­kirkju í dag. ",
	"Atli@Eiður.is"],
]

@app.route('/')
def index():
	return render_template("index.tpl", frettir=frettir)

@app.route("/frett/<int:nr>")
def frett0(nr):
	frett = frettir[nr]
	return render_template("info.tpl",frett=frett)

@app.errorhandler(404)
def error404(error):
	return "Síðan var ekki fundin", 404

if __name__ == "__main__":
	app.run(debug=True)