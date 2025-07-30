class TarjetaCredito:
    # Constructor de la clase
    def __init__(self, limite_credito, intereses, monto=0):
        """
        Inicializa una nueva instancia de TarjetaCredito.
        
        :param limite_credito: Límite de crédito de la tarjeta.
        :param intereses: Tasa de interés (como decimal).
        :param monto: Monto inicial (opcional, default es 0).
        """
        self.saldo_pagar = monto if monto <= limite_credito else 0  # Asegura que el saldo no exceda el límite
        self.limite_credito = limite_credito
        self.intereses = intereses

    # Método para realizar compras
    def compra(self, monto):
        """
        Realiza una compra con la tarjeta si no se ha alcanzado el límite de crédito.
        
        :param monto: Monto de la compra.
        """
        if self.saldo_pagar + monto <= self.limite_credito:
            self.saldo_pagar += monto
        else:
            print("Tarjeta Rechazada, has alcanzado tu límite de crédito.")

    # Método para realizar pagos
    def pago(self, monto):
        """
        Realiza un pago a la tarjeta reduciendo el saldo a pagar.
        
        :param monto: Monto del pago.
        """
        if self.saldo_pagar >= monto:
            self.saldo_pagar -= monto
        else:
            print("Pago rechazado, el monto supera el saldo a pagar.")

    # Método para mostrar información de la tarjeta
    def mostrar_info_tarjeta(self):
        """
        Imprime la información actual de la tarjeta en la consola.
        """
        print(f"Saldo a Pagar: ${self.saldo_pagar:.2f}")

    # Método para cobrar intereses
    def cobrar_interes(self):
        """
        Agrega intereses al saldo a pagar basándose en la tasa de interés.
        """
        interes_generado = self.saldo_pagar * self.intereses
        self.saldo_pagar += interes_generado


# Crear 3 tarjetas según las instrucciones
tarjeta1 = TarjetaCredito(limite_credito=500, intereses=0.02)
tarjeta2 = TarjetaCredito(limite_credito=1000, intereses=0.015)
tarjeta3 = TarjetaCredito(limite_credito=800, intereses=0.025)

# Operaciones para la primera tarjeta
tarjeta1.compra(100)  # Compra 1
tarjeta1.compra(200)  # Compra 2
tarjeta1.pago(50)     # Pago
tarjeta1.cobrar_interes()  # Cobrar intereses
tarjeta1.mostrar_info_tarjeta()  # Mostrar información

# Operaciones para la segunda tarjeta
tarjeta2.compra(300)  # Compra 1
tarjeta2.compra(400)  # Compra 2
tarjeta2.compra(500)  # Compra 3
tarjeta2.pago(200)    # Pago 1
tarjeta2.pago(100)    # Pago 2
tarjeta2.cobrar_interes()  # Cobrar intereses
tarjeta2.mostrar_info_tarjeta()  # Mostrar información

# Operaciones para la tercera tarjeta
tarjeta3.compra(150)  # Compra 1
tarjeta3.compra(250)  # Compra 2
tarjeta3.compra(350)  # Compra 3
tarjeta3.compra(450)  # Compra 4
tarjeta3.compra(550)  # Compra 5 (Excede el límite)
tarjeta3.mostrar_info_tarjeta()  # Mostrar información


#BONUS
class TarjetaCredito:
    # Lista estática para almacenar todas las tarjetas
    todas_las_tarjetas = []

    def __init__(self, limite_credito, intereses, monto=0):
        # ... (resto del constructor)
        TarjetaCredito.todas_las_tarjetas.append(self)

    @classmethod
    def mostrar_todas_las_tarjetas(cls):
        """
        Muestra la información de todas las tarjetas creadas.
        """
        for i, tarjeta in enumerate(cls.todas_las_tarjetas, start=1):
            print(f"\nTarjeta {i}:")
            tarjeta.mostrar_info_tarjeta()

# Después de crear todas las tarjetas
TarjetaCredito.mostrar_todas_las_tarjetas()