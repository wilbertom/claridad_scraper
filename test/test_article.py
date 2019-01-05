from unittest import TestCase
from datetime import datetime

from test.support.files import support_file_contents

from claridad import Article


class TestArticle(TestCase):

    def setUp(self):
        self.maxDiff = None

        self.article_1 = Article(1, support_file_contents('article_1.html'))
        self.article_2 = Article(2, support_file_contents('article_2.html'))
        self.article_3 = Article(3, support_file_contents('article_3.html'))

    def test_it_sets_the_uid(self):
        self.assertEquals(self.article_1.id, 1)
        self.assertEquals(self.article_2.id, 2)
        self.assertEquals(self.article_3.id, 3)


    def test_getting_the_content_id(self):
        self.assertEquals(self.article_1.content_id, 'B591783CAE5850FBAB1C6DE435674D37')

    def test_getting_the_article_title(self):
        self.assertEquals(self.article_1.title, 'La cazadora y  su monstruo Halloween (2018)')

    def test_getting_the_article_body(self):
        body = '\n\n'.join([
            "El horror es uno de mis géneros favoritos. Me encantan los monstruos, especialmente cuando éstos cuestionan nuestra propia humanidad. No hay nada más poderoso que mirarnos y descubrirnos desde la otredad. Mis monstruos favoritos son aquéllos que desafían las normas impuestas en una sociedad dividida entre los privilegiados y los desposeídos. En una película como Las brujas de Zugarramurdi (dir. Alex de la Iglesia, España/Francia, 2013), dos asaltantes escapan de la policía y se ven obligados a cruzar un pueblo donde habitan brujas poderosas. Durante el atraco, uno se disfrazó de un Cristo color plata y el otro de un soldado de plástico cubierto de verde. En Zugarramurdi, las brujas no atacarán a dos inocentes ladrones, sino a los símbolos de un sistema opresivo masculino representado por la iglesia (el Cristo de plata) y la milicia (el soldado de plástico). La feminidad mítica y oscura hará temblar al patriarcado sin compasión. No me identifico con estas brujas sólo porque son actuadas por dos actrices españolas que me fascinan, Carmen Maura y Terele Pávez, sino porque su repulsión a la norma resuena en mí. Sin embargo, no siento empatía por un monstruo como Michael Myers, el cuco que atormenta a Laurie Strode (Jamie Lee Curtis) en la serie de Halloween. Este es un depredador obsesionado con una mujer que victimiza y quiere ver morir.",
            "La nueva película de Halloween (dir. David Gordon Greer, EEUU, 2018) no utiliza un número para identificarse en la serie ya que no tiene nada que ver con las seis secuelas de la original (sin contar Halloween III: Season of the Witch [dir. Tommy Lee Wallace, EEUU, 1982], que no continúa la historia de Strode y Myers) ni con los remakes de Rob Zombie. Esta última es una secuela directa de Halloween (dir. John Carpenter, EEUU, 1978). Después de los asesinatos en los suburbios de Haddonfield, Illinois, Michael Myers fue recluido en el hospital mental de donde había escapado en la original. Myers no es inmortal a lo Jason Vorhees de la serie de Friday the 13th. Este se asemeja más a Max Cady (Robert De Niro) en Cape Fear (dir. Martin Scorsese, EEUU, 1991), cuya obsesión por castigar a su abogado defensor (Nick Nolte) lo ha inmunizado al dolor físico y lo ha ayudado a escapar de la muerte. Myers sobrevive los balazos, un gancho en un ojo y una caída de un segundo piso porque Laurie sigue viva. Y él no lo puede permitir.",
            "Cuarenta años después de sobrevivir los horrores de la primera película y de haber perdido amistades a manos de Myers, Laurie es una mujer que sufre de trastorno de estrés postraumático. Esto la ha llevado a preocuparse constantemente por su propia seguridad tanto como la de su hija (Judy Greer) y la de su nieta (Andi Matichak). Laurie ha pasado cuatro décadas preparándose para lo que ella ve como el inevitable encuentro final con Myers. La Laurie de la primera película es una adolescente algo tímida y enfocada en sus estudios que no le interesa la exploración sexual de su amiga. De hecho, los expertos en el subgénero del slasher argumentan que la razón por la que Laurie se salva es porque mantuvo su virginidad. Sin embargo, su inocencia terminó ese 31 de octubre de 1978. La Laurie que vemos el 31 de octubre de 2018 lleva un rifle en mano y tiene una casa preparada para capturar y matar al depredador que la persigue. En su trayectoria, el personaje de Jamie Lee Curtis nos recuerda a Sarah Connor (Linda Hamilton) en Terminator2: Judgment Day (dir. James Cameron, EEUU, 1991). La feliz e ingenua Sarah de Terminator (dir. James Cameron, EEUU 1984), se ha transformado en la secuela en una mujer preparada para sobrevivir un apocalipsis creado por la tecnología que erradicará a la humanidad. Igual que Connor, Laurie se ha endurecido por el trauma sufrido y no descansará hasta que Myers haya muerto.",
            "Halloween (2018) hace constantes referencias a la película original. De hecho, planifico verla de nuevo porque no he visto Halloween (1978) en unos años y quiero estudiar más de cerca el diálogo visual entre ambas. Halloween (2018) ha sido la secuela que siempre había deseado. Sus escritores, Danny McBride, Jeff Fradley y David Gordon Green, han sido conocidos por sus trabajos en la comedia. Su gusto por el trabajo de John Carpenter los llevó a crear una obra que reconoce las maravillas de la original, sin perder la oportunidad de explorar de maneras innovadoras la historia de Laurie. Mi único problema es con algunos momentos de humor. Reconozco y disfruto del humor raro y oscuro del horror (de la Iglesia es un maestro de esto en el cine de horror español). Sin embargo, hay momentos en Halloween (2018) en los cuales el director trata de combinar algo jocoso con un asesinato terrible, minimizando el sufrimiento de la víctima y entorpeciendo su impacto en el espectador. Pero estos momentitos no le restan a lo que considero la secuela perfecta de Halloween (1978).",
            "No puedo terminar sin comentar sobre las maravillosas actuaciones de James Jude Courtney y Nick Castle en el personaje de Myers y de Jamie Lee Curtis. Castle fue el primer actor en hacer de Michael Myers y le da un lenguaje corporal muy particular. Su Myers es una simple pared sin emociones, cuyos movimientos lentos y precisos lo convierten en una maldición ineludible. Por otro lado, mientras la Laurie de la primera película corre despavorida y enfrenta al depredador con la desesperación de una víctima que lucha por sobrevivir un ataque; la Laurie mayor es una cazadora en pleno control de sus emociones y de su cuerpo. Myers no ha cambiado, pero Laurie ya no es víctima. No les estoy dañando la sorpresa cuando les digo que el encuentro final entre Myers y Laurie es la conclusión más apropiada para una saga sobre una mujer que sobrevive lo indecible. Halloween (2018) refleja nuestros tiempos porque aquella víctima de la primera mirará al monstruo a los ojos y éste temblará por el horror que le espera.",
        ])

        self.assertEquals(
            self.article_1.body,
            body
        )

    def test_getting_the_pdf_link(self):
        self.assertEquals(
            self.article_1.pdf_link,
            'http://www.claridadpuertorico.com/contentpdf.html?news=B591783CAE5850FBAB1C6DE435674D37'
        )

    def test_getting_the_date_published(self):
        date = datetime(2018, 10, 30)

        self.assertEquals(
            self.article_1.date_published,
            date
        )

    def test_getting_the_date_published_when_it_is_before_the_byline(self):
        date = datetime(2018, 11, 28)

        self.assertEquals(
            self.article_2.date_published,
            date
        )

    def test_getting_the_author_name(self):
        self.assertEquals(
            self.article_1.author_name,
            'Juan R. Recondo'
        )

    def test_getting_the_author_name_when_it_is_in_the_freaking_body_itself(self):
        self.assertEquals(
            self.article_2.author_name,
            'Katu Arkonada'
        )

    def test_is_summary_is_false_for_full_articles(self):
        self.assertFalse(self.article_1.is_summary)
        self.assertFalse(self.article_2.is_summary)

    def test_is_summary_is_true_for_articles_that_require_a_login(self):
        self.assertTrue(self.article_3.is_summary)
